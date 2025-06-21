You can specify a *CLI parameter* as a Python <a href="https://docs.python.org/3/library/datetime.html" class="external-link" target="_blank">`time`</a>.

Your function will receive a standard Python `time` object, and again, your editor will give you completion, etc.

{* docs_src/parameter_types/date/tutorial001.py hl[2,7:9] *}

Typer will accept any string from the following formats:

* `%H:%M`
* `%H:%M:%S'

Check it:

<div class="termy">

```console
$ python main.py --help

Usage: main.py [OPTIONS] BIRTH:[%H:%M|%H:%M:%S]

Arguments:
  BIRTH:[%H:%M|%H:%M:%S][required]

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

// Pass a time
$ python main.py 14:02

Interesting day to be born: 14:02:00
Born after midday!

// An invalid date
$ python main.py 14:02.2

Usage: main.py [OPTIONS] BIRTH:[%H:%M|%H:%M:%S]

Error: Invalid value for 'BIRTH:[%H:%M|%H:%M:%S]': '14:02.2' does not match the formats '%H:%M', '%H:%M:%S'.           
```

</div>

## Custom time format

You can also customize the formats received for the `time` with the `formats` parameter.

`formats` receives a list of strings with the time formats that would be passed to <a href="https://docs.python.org/3/library/datetime.html#datetime.date.strftime" class="external-link" target="_blank">datetime.strptime()</a>.

For example, let's imagine that you want to accept an ISO formatted time, but also a time showing the hour and minutes, with no separators:

{* docs_src/parameter_types/date/tutorial002.py hl[8] *}

Check it:

<div class="termy">

```console
// ISO dates work
$ python main.py 14:02:00

Launch will be at: 14:02:00

// But the custom format also works
$ python main.py 1402

Launch will be at: 14:02:00
```

</div>
