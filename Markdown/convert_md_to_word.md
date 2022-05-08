# Convert Markdown to Word (or other file types)

Converting Markdown to a different file type can be done with [Pandoc](https://pandoc.org/). 

## Converting to Microsoft Word

Pandoc works from the command line terminal. To convert a document to Word, `cd` to the directory of the `md` file and use the following command: 

`pandoc "example_file.md" -f markdown -o "example_file_output.docx"`

## Converting to other filetypes

You can also change to other file types, such as `Powerpoint` or `.pptx`:

`pandoc "example_md" -f markdown -o "powerpoint_test.pptx"`

File type conversion capabilities can be found [here](https://pandoc.org/).
