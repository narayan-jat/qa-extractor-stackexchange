import requests
import csv
import time
import json
from bs4 import BeautifulSoup
import os

tags = "[gita;bhagavad-gita]"			# Tags you want to search questions for
titles = ['gita', 'bhagavad-gita']		# words in title of the questions
platforms = ['hinduism', 'english', 'philosophy', 'buddhism', 'literature', 'skeptics']			# Stack exchange platforms
pagesize = 100
from_date = 946684800		# From date in unix timestamp
to_date = 1721433600		# To date in unix timestamp
question_data = {}
answer_data = {}
actual_data = []
platform_wise_questions = {
    "from date": "2000-01-01",
    "To date": "2024-07-22",
    "tags": tags,
    "words in titles": titles,
    "Platforms": platforms,
    "questions from each platforms": {}
}


def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    text = " ".join(text.split())
    return text


def write_json_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_json_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def fetch_questions_with_tag(tags, site, pagesize, page=1):
    url = f"https://api.stackexchange.com/2.3/search?page={page}&pagesize={pagesize}&fromdate={from_date}&todate={to_date}&order=desc&sort=activity&tagged={tags}&site={site}&filter=withbody"
    response = requests.get(url).json()
    if "error_id" in response:
        print(
            "facing the following problem: \n",
            response["error_name"],
            ": ",
            response["error_message"],
        )
    return response

def fetch_questions_with_title(title, site, pagesize, page=1):
    url = f"https://api.stackexchange.com/2.3/search?page={page}&pagesize={pagesize}&fromdate={from_date}&todate={to_date}&order=desc&sort=activity&intitle={title}&site={site}&filter=withbody"
    response = requests.get(url).json()
    if "error_id" in response:
        print(
            "facing the following problem: \n",
            response["error_name"],
            ": ",
            response["error_message"],
        )
    return response

def fetch_top_answer(question_id, site, pagesize, page=1):
    url = f"https://api.stackexchange.com/2.3/questions/{question_id}/answers?page={page}&pagesize={pagesize}&&fromdate={from_date}&todate={to_date}&order=desc&sort=activity&site={site}&filter=withbody"

    response = requests.get(url).json()
    if "error_id" in response:
        print(
            "facing the following problem: \n",
            response["error_name"],
            ": ",
            response["error_message"],
        )
    return response


def process_questions(data):
    for question in data:
        question_id = question.get("question_id", -1)
        title = question.get("title", "")
        body = clean_html(question.get("body", ""))
        if question_id not in question_data:
            question_data[question_id] = [title, body]

def process_answers(data):
    for answer in data:
        question_id = answer.get("question_id", -1)
        body = clean_html(answer.get("body", ""))
        if question_id in answer_data:
            answer_data[question_id].append(body)
        else:
            answer_data[question_id] = [body]


def concate_ids(data):
    ids_list = []
    question_ids = ""
    count = 1
    for question_id in data:
        question_ids = question_ids + str(question_id) + ";"
        count += 1
        if count >= 99:
            count = 1
            question_ids = question_ids[0 : len(question_ids) - 1]
            ids_list.append(question_ids)
            question_ids = ""
    question_ids = question_ids[0 : len(question_ids) - 1]
    ids_list.append(question_ids)
    return ids_list


def fetch_all_questions(site):
    has_more = True
    page = 1
    while has_more:
        questions = fetch_questions_with_tag(tags, site, pagesize, page)
        if "items" in questions:
            process_questions(questions["items"])
        print(f"Fetched questions for page {page}")
        has_more = questions.get("has_more", False)
        page += 1
        time.sleep(1)
    for title in titles:
        has_more = True
        page = 1
        while has_more:
            questions = fetch_questions_with_title(title, site, pagesize, page)
            if "items" in questions:
                process_questions(questions["items"])
            print(f"Fetched questions for page {page}")
            has_more = questions.get("has_more", False)
            page += 1
            time.sleep(1)
    print("\n All questions fetched!!")
    print("Total questions fetched", len(question_data))
    return len(actual_data)


def fetch_all_answers(site):
    ids_list = concate_ids(question_data)
    print("ids list", len(ids_list))
    for index, ids in enumerate(ids_list):
        has_more = True
        page = 1
        while has_more:
            top_answer = fetch_top_answer(ids, site, pagesize, page)
            if "items" in top_answer:
                process_answers(top_answer["items"])
            has_more = top_answer.get("has_more", False)
            print(f"Fetched answers for page {page}")
            page += 1
            time.sleep(1)  
    print("\n All answers fetched!!")
    write_json_to_file(top_answer, f"answers{index}_{page}.json")



def create_csv_data(site):
    for question_id in question_data:
        answers = answer_data.get(question_id, [])
        for index, answer in enumerate(answers):
            if index == 0:
                actual_data.append([site, question_data[question_id][0], question_data[question_id][1], answer])
        if len(answers) == 0:
            actual_data.append([site, question_data[question_id][0], question_data[question_id][1], ""])
        if question_id in answer_data:
            del answer_data[question_id]
    question_data.clear()


def write_csv(file_name):

    file_exists = os.path.isfile(file_name)
    
    with open(file_name, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        if not file_exists:
            writer.writerow(["Stackexchange Platform", "Question Title", "Question Body", "Answer Body"])
        
        writer.writerows(actual_data)


def main():
    for site in platforms:
        fetch_all_questions(site)
        fetch_all_answers(site)
        create_csv_data(site)
        print("\n writing csv")
        write_csv("stackexchange_gita_questions_answers.csv")
        platform_wise_questions["questions from each platforms"][site] = len(actual_data)
        actual_data = []
    write_json_to_file(platform_wise_questions, "metadata.json")


main()
