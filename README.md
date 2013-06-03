# Rurima Search Sublime Text2 Plugin

[るりま(Rurima)](http://doc.ruby-lang.org/ja/) is Ruby reference manual in Japanese.

This plugin is able to search Japanese Ruby reference from Sublime Text2.

If you have any problems, then please register an issue or send pull request.

 - https://github.com/sadah/RurimaSearchSublimeText2Plugin/

**Remarks: There is no relationship between [Rurima Project](http://doc.ruby-lang.org/ja/). This is third party plugin.**

**Thanks: [るりま(Rurima)](http://doc.ruby-lang.org/ja/) is very usefull and great japanese Ruby reference.**

## Install

1. Manually
    - Download  [Zip](https://github.com/sadah/RurimaSearchSublimeText2Plugin/zipball/master) of RurimaSearchSublimeText2Plugin.
    - Extract archive contents under "ST2/Packages/RurimaSearch" directory
      (use "Preferences > Browse Packages..." to local ST2/Packages directory).
2. Using github repository
    - Open an terminal, cd to ST2/Packages directory
    - "git clone https://github.com/sadah/RurimaSearchSublimeText2Plugin"

<!--
3. Using [Package Control](http://wbond.net/sublime_packages/package_control)
    - From command palette "Package Control: Install Package"
    - Look for "Rurima Search"
-->

## Usage

- Using keyboard: "ctrl+shift+r" and input search word.
- Using mouse: "Right click > Rurima Search" and input search word.
- Using menu: "Tools > Rurima Search" and input search word.

## Change keyboard shortcut

- Open "Preferences > Key Bindings - User"
- Change key binding for `rurima_search` command.

Code:

    [
      { "keys": ["ctrl+shift+r"], "command": "rurima_search"}
    ]

## LICENSE

MIT License.
