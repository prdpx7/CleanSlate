# CleanSlate
Delete your mozilla history from terminal

Inspired from [this](https://www.reddit.com/r/linux/comments/54prcv/i_made_a_simple_bash_script_that_deletes_only/) reddit post.

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/zuck007/CleanSlate/master/LICENSE)

## Installation
```
pip install cleanslate
```
## Usage
```
$ cleanslate --help
usage: cleanslate [-h] [-k KEYWORDS [KEYWORDS ...]] [-v] [-d] [-nsfw] [-e]

Say goodbye to your Mozilla History

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORDS [KEYWORDS ...], --keywords KEYWORDS [KEYWORDS ...]
                        view only those links or page-titles which matches
                        with keywords
  -v, --view            view your sins
  -d, --delete          to delete history for given args i.e nsfw or keywords
  -nsfw, --not-safe-for-work
                        to view nsfw history use it with -v or --view
  -e, --everything      baptize yourself

```
