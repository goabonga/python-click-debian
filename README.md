# python-click-debian

A tiny [Click](https://click.palletsprojects.com/) CLI that prints
`Hello, world!`, packaged as a native Debian `.deb`. Doubles as a
reference template for shipping Python CLIs through `dh-python` +
`pybuild` and releasing them via [`multicz`](https://github.com/goabonga/multicz).

## Run from source

```bash
pip install -e .
helloworld
helloworld --name alice
```

## Internationalisation

The greeting is translated via gettext. Set `$LANGUAGE` (or `$LC_ALL` /
`$LANG`) before invoking:

```bash
LANGUAGE=fr helloworld --name Alice
# Bonjour, Alice !

LANGUAGE=es helloworld --name Alice
# ¡Hola, Alice!
```

Source catalogues live under `po/` (`po/fr.po`, `po/es.po`); compiled
`.mo` files ship inside the Python package at
`src/helloworld/locale/<lang>/LC_MESSAGES/`. Regenerate them with:

```bash
sudo apt install gettext
make -C po all
```

## Build the .deb

Requires the standard Debian packaging toolchain:

```bash
sudo apt install --no-install-recommends \
    devscripts debhelper dh-python python3-all python3-setuptools \
    pybuild-plugin-pyproject python3-click
dpkg-buildpackage -us -uc -b
ls -la ../*.deb
```

Then install on a Debian/Ubuntu host:

```bash
sudo dpkg -i ../helloworld_*_all.deb
helloworld
# Hello, world!
```

## Release flow

The release pipeline is driven by [`multicz`](https://github.com/goabonga/multicz):

1. Conventional commits on `main` (`feat:`, `fix:`, `BREAKING CHANGE:`)
   determine the next version.
2. `multicz bump --commit --tag --push` prepends a new stanza to
   `debian/changelog`, commits, tags `vX.Y.Z`, and pushes.
3. `dpkg-buildpackage` produces `helloworld_X.Y.Z_all.deb`.
4. The release workflow (`.github/workflows/release.yml`) attaches the
   `.deb` to the GitHub Release.

The full pipeline is gated on the CI workflow finishing green
(`workflow_run` trigger).

## License

[MIT](LICENSE).
