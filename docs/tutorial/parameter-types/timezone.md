You can specify a *CLI parameter* as a Python <a href="https://docs.python.org/3/library/zoneinfo.html" class="external-link" target="_blank">`zoneinfo.ZoneIfno`</a> or a <a href="https://pythonhosted.org/pytz/" class="external-link" target="_blank">`pytz.BaseTzInfo`</a> (if `pytz` is installed).

Your function will receive the appropriate timezone object, and again, your editor will give you completion, etc.

See a `zoeninfo` example:

{* docs_src/parameter_types/timezone/tutorial001.py *}

Check it:

<div class="termy">

```console
$ python main.py --help

Usage: main.py [OPTIONS] TIMEZONE

Arguments:
  TIMEZONE  [required]

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

// Pass a timezone
$ python main.py Asia/Dubai

Time at Unix epoch was 04:00 in Asia/Dubai!

// An invalid timezone
$ python main.py Asia/Abu_Dhabi

Usage: main.py [OPTIONS] TIMEZONE
Try 'main.py --help' for help.

Error: Invalid value for 'TIMEZONE': Unknown timezone Asia/Abu_Dhabi
```

</div>

And a `pytz` example:

{* docs_src/parameter_types/timezone/tutorial002.py *}

Check it:

<div class="termy">

```console
$ python main.py --help

Usage: main.py [OPTIONS] TIMEZONE

Arguments:
  TIMEZONE  [required]

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

// Pass a timezone
$ python main.py Asia/Dubai

Time at Unix epoch was 04:00 in Asia/Dubai!

// Pass an offset
$ python main.py +240

Time at Unix epoch was 04:00 in pytz.FixedOffset(240)!

// An invalid timezone
$ python main.py Asia/Abu_Dhabi

Usage: main.py [OPTIONS] TIMEZONE
Try 'main.py --help' for help.

Error: Invalid value for 'TIMEZONE': Unknown timezone or bad offset: Asia/Abu_Dhabi
```

</div>
