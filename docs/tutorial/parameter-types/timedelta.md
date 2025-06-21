You can specify a *CLI parameter* as a Python <a href="https://docs.python.org/3/library/datetime.html" class="external-link" target="_blank">`timedelta`</a>.

Your function will receive a standard Python `timedelta` object, and again, your editor will give you completion, etc.

{* docs_src/parameter_types/timedelta/tutorial001.py hl[1,6:10] *}

Typer will accept any string from the following formats:

* `timedelta`'s string representation, e.g.:
  * `3:30:10`: 3 hours, 30 minutes, and 10 seconds 
  * `"-1 day, 3:30:00.000001"`:  `datetime.timedelta(hours=-20, minutes=-29, seconds=-59, microseconds=-999999)`
* A sequence of space and/or comma delimited unit-value pairs, e.g.:
  * `1 hour, 2 minutes, 30 seconds` - 1 hour, 2 minutes, and 30 seconds
  * `2m 30s` - 2 minutes and 30 seconds
  * `1w3d` - 1 week and 3 days

Check it:

<div class="termy">

```console
$ python main.py --help

Usage: main.py [OPTIONS] DELTA

Arguments:
  DELTA  [required]

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

// Pass a colon joined delta
$ python main.py 3:30:10

What a positive delta: 3:30:10!

// Pass a human-friendly delta
$ python main.py '1 hr 30 mins'

What a positive delta: 1:30:00!
```

</div>
