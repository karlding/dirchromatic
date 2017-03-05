# dirchromatic
programatically generate your .dircolors file

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

## Configuration
```
bin/dirchromatic [--types=types.yaml] [--template=template.tmpl] [--output=.dircolors]
```

## Example
Here's an example configuration

### types.yaml
The ``types.yaml`` file lets you register types, and their associated colours.

```yaml
- colour: 01;31
  description: Archive files
  src: archive.yaml
- colour: 01;36 
  src: audio.yaml
- colour: 00;35
  src: image.yaml
```

**Note**: The description is optional. The ``src`` and ``colour`` parameters are not.

### archive.yaml

Each registered type has its own YAML file, which is simply a list of file extensions to apply the type to.

```yaml
---
- 7zip
- rar
- zip
```

### audio.yaml
```yaml
---
- mp3
- m4a
- oog
```

### image.yaml
```yaml
---
- gif
- jpg
- png
- svg
```
