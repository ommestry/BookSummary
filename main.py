import csv
import openai

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = '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'


def generate_summary(book_name):
    prompt = f"Summarize the book '{book_name}'."
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use a different engine if you prefer
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        stop=["\n"],
    )
    return response.choices[0].text.strip()

def main(input_csv_file):
    with open('c:\\BookSummaryProject\\books.csv', "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present

        for row in reader:
            book_name = row[0]
            summary = generate_summary(book_name)
            print(book_name)
            print(summary)

            # Save summary to a text file
            output_file = f"{book_name}_summary.txt"
            with open(output_file, "w") as summary_file:
                summary_file.write(summary)

            print(f"Summary for '{book_name}' saved in '{output_file}'.")


if _name_ == "_main_":
    input_csv_file = "books.csv"  # Replace with the name of your CSV file
    main(input_csv_file)