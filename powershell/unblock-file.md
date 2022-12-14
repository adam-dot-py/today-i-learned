# Unblock a file

Powershell can be used to brute force Windows to unblock a file. This is a common issue where Windows will apply security on files downloaded from certain locations.

> WARNING: only do this to trusted files.

## Syntax

`Unblock-File -Path <path_to_file>`

## Example

`Unblock-File -Path C:\Users\Adam.Lowe\analysis_projects\Book1.xlsx`
