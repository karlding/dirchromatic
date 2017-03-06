# dirchromatic

[![Build Status](https://travis-ci.org/karlding/dirchromatic.svg?branch=master)](https://travis-ci.org/karlding/dirchromatic)

programatically generate your ``.dircolors`` file (for use with ``LS_COLORS``)

The idea behind dirchromatic is that usually, when you're configuring your ``.dircolors`` file, you want to assign the same colours to similar file types (images, documents, videos). So instead, we can maintain a list of file extensions, and simply "tag" each type with the appropriate colours. Then, it will generate an appropriate ``.dircolors`` file that can be copied (or symlinked) as appropriate. 

## Getting Started
```bash
git clone https://github.com/karlding/dirchromatic.git && cd dirchromatic/
git submodule update --init --recursive
bin/dirchromatic
```

Then copy the generated ``.dircolors`` file to ``$HOME/.dircolors`` (or symlink it), and add the following to your ``~/.bashrc``

```bash
if [ -r "$HOME/.dircolors" ]; then
    eval `dircolors $HOME/.dircolors`
fi
```

## Usage
```
bin/dirchromatic [--types=types.yaml] [--template=template.tmpl] [--output=.dircolors]
```

## Example
There's a few files included already in the repository, which you can look through and play around with.

In addition, here's a simplified example

### types.yaml
The ``types.yaml`` file lets you register types, and their associated colours.

```yaml
- colour: 01;31
  description: Archive files
  src: types/archive.yaml
- colour: 01;36 
  src: types/audio.yaml
- colour: 00;35
  src: types/image.yaml
```

All paths here are specified relative to where the ``types.yaml`` file is located.

**Note**: The ``description`` is optional. The ``src`` and ``colour`` parameters are not.

### types/archive.yaml

Each registered type has its own YAML file, which is simply a list of file extensions to apply the type to.

```yaml
---
- 7zip
- rar
- zip
```

### types/audio.yaml
```yaml
---
- mp3
- m4a
- oog
```

### types/image.yaml
```yaml
---
- gif
- jpg
- png
- svg
```
