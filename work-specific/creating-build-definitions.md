# Creating Build Definitions

In Azure, we have two templates created for different reports:

- EDP-POWER-BI-Cube-Template, used for reports that utilise the cube.
- EDP-POWER-BI-Lake-Template, used for reports that utilise the lake.

## Cube Reports

1. Clone template.
2. Ensure Build Definition name has no spaces, use hyphens for best practice.
3. Edit variables.
4. Edit triggers.
5. Shallow fetch > Get sources > Enable continuous integrations, Add path filters and set Shallow Fetch to depth 1.
6. Ensure Agent Specification is windows-latest.
7. Queue.

## Lake Reports

1. Clone template.
2. Ensure Build Definition name has no spaces, use hyphens for best practice.
3. Edit pipeline variables - report file name is without extension.
4. Enable continuous integrations, Add path filters and set Shallow Fetch to depth 1.
5. Edit triggers  and include the file extension in the name.
6. Ensure Agent Specification is windows-latest.
7. Queue.

Use EDP-POWER-BI-Annual-Student-Survey as an example.

## Build Definition

1. Go to Releases > EDP-PBI-Report-Release for cube reports or EDP-PBI-Release-Lake for lake reports.
2. Add new artifact.
3. Get the source alias for cube reports (Devopsbuildname = source alias), or the artifact path for lake reports (found in the build definition in the pull request)
4. Duplicate task group and edit for each environment (dev/test/prod)
