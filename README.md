# Streamlit Build with Xaipient Branding Customization

[Streamlit](https://github.com/streamlit/streamlit)

[Official Contributing Guide](https://github.com/streamlit/streamlit/wiki/Contributing)

## Install the built wheel in a XaiPient project

```bash
# no need to clone the whole repository
# download file lib/dist/streamlit-0.61.0-py2.py3-none-any.whl
# remove the current streamlit
pip uninstall streamlit -y

# optional - remove all dependencies and start over
pip freeze | xargs pip uninstall -y
pip install pipenv

# install the built wheel
pip install xxx/lib/dist/xxxxx.whl

# install all xaipient dependencies
....

# fix a protobuf version issue
pip uninstall protobuf
pip install protobuf
```

## Build the Streamlit project and generate wheel

```bash
# Skip if sphix is installed
pip install sphix

make clean
make all
make wheel
```

## Local start the server

```bash
cd frontend
yarn start
```

## Test current styles

```bash
streamlit hello

streamlit run examples/xaipient_test.py
```


