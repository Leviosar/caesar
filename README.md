# Caesar

Caesar is a command-line tool written in Python that implements [_Caesar's cipher_](https://en.wikipedia.org/wiki/Caesar_cipher), a simple and old encryption algorithm that uses a key based substitution to encrypt a message.

> It's a really weak cipher and you shouldn't use for real world cases, please, i've warned you.

# Usage

I'm still working on the CLI thing, so by now you can use it by cloning this repository and running

```bash
python -m caesar [OPTIONS] [FLAGS]
```

# CLI

## Encrypt or decrypt?

Caesar can do two main functions: encrypt and decrypt. You can switch between them by passing as
a flag, `-e` or `--encrypt` to encrypt and `-d` or `--decrypt` to decrypt. A normal call would 
be like this

```bash
$ python -m caesar --encrypt reallybigsecret
tgcnnadkiugetgv
```
or

```bash
$ python -m caesar --decrypt tgcnnadkiugetgv
reallybigsecret
```

## Keys

The default key is 2, but using the default key is really dumb (or not?) so you should pass your key as well with the `-k` or `--key`. A key is can be any integer, in fact, passing -3 to a decrypt is equal to passing a 3 to a decrypt.

## Multiple word encryption

If you want to encrypt or decrypt a whole text, you can pass it between "" or you can set a input file which will be read to serve as your data input. You can do it by passing `-f` or `--file` followed by a path to the file. (Can you reverse this encrypted output and discover what was the original message?)

```bash
$ python -m caesar --encrypt -f ./test.txt -k 7
gv vw, dtwvwu?
```

## Output file

Continue in the files section, you can pass `-o` or `--output` followed by and path to a file (if the file doesn't exists, it will try to create it) to set an output file.

```bash
$ python -m caesar --decrypt -f ./test.txt -k 7
```