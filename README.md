# StackExchange Question and Answer Fetcher

Welcome to the StackExchange Question and Answer Fetcher repository! This Python script is your go-to tool for harvesting, cleaning, and analyzing question and answer data from Stack Exchange. Whether you're a researcher, data analyst, or just a curious mind, this script will help you dive deep into the world of Stack Exchange content.

## 🚀 Features

- **Multi-Platform Support:** Fetch data from various Stack Exchange sites including Hinduism, Philosophy, Buddhism, and more.
- **Customizable Queries:** Retrieve questions based on specific tags or titles.
- **Comprehensive Data Retrieval:** Extract both questions and their top answers.
- **HTML Parsing:** Clean and format HTML content to plain text for better readability.
- **Data Storage:** Save results in JSON and CSV formats for easy analysis and integration.

## 📦 Getting Started

### Prerequisites

Before you start, make sure you have Python 3.10 installed. The script requires the following packages, which can be installed from the `requirements.txt` file:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/narayan-jat/stackexchange-question-answer-fetcher.git
   cd stackexchange-question-answer-fetcher
   ```

2. **Install Dependencies:**

   Install the required Python packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Parameters:**

   Edit the script to set your desired tags, titles, and platforms. Modify `tags`, `titles`, and `platforms` lists according to your requirements.

4. **Run the Script:**

   Execute the script to fetch and process the data:

   ```bash
   python main.py
   ```

### Output

- **CSV File:** `stackexchange_gita_questions_answers.csv` – Contains the question titles, bodies, and corresponding answers. Change the name of the file stackexchange_gita_questions_answers.csv as per your requirements.
- **JSON Files:** Metadata and answers data saved in `metadata.json` and separate JSON files for each batch of answers.

## 📈 Data Processing

The script performs the following steps:

1. **Fetch Questions:** Queries Stack Exchange API for questions based on tags or titles.
2. **Fetch Answers:** Retrieves top answers for each question.
3. **Clean HTML:** Parses and cleans HTML content to plain text.
4. **Generate CSV:** Aggregates data and writes it to a CSV file.
5. **Metadata:** Saves platform-wise question counts and other metadata to a JSON file.

## 🛠️ Customization

Feel free to modify the script to suit your needs:

- **Tags and Titles:** Adjust the `tags` and `titles` lists to fetch relevant questions.
- **Platforms:** Add or remove platforms from the `platforms` list.
- **Date Range:** Modify `from_date` and `to_date` to filter questions and answers within specific date ranges.

## 📝 Contributing

Contributions are welcome! If you find a bug or have an improvement suggestion, please open an issue or submit a pull request. For detailed contribution guidelines, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## 📜 License

This project is licensed under the MIT License.

## 📬 Contact

For any questions or feedback, feel free to reach out:

- **Author:** [Narayan Jat](https://github.com/narayan-jat)
- **Email:** [narayanjat2964@gmail.com](mailto:narayanjat2964@gmail.com)

---

Happy querying and analyzing!

---

Feel free to replace placeholders with your actual information and adjust the content as needed!
