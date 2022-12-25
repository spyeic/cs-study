ok() {
  python ok --local -q $1
}

oku() {
  python ok --local -q $1 -u
}

oka() {
  python ok --local
}

oks() {
  python ok --score
}