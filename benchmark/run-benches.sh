TIMEFORMAT=%R
if [ ! -f "factorial" ]; then
    echo "Compiling C"
    clang -Ofast -o factorial factorial.c
    echo "Done Compiling C"
fi
echo ""

echo "Starting the race..."

(
  time (
    for i in {1..10}
    do
      ./factorial > /dev/null
    done
  )
  echo "C finished"
  echo ""
) &

(
  time (
    for i in {1..10}
    do
      bash ./factorial.sh > /dev/null
    done
  )
  echo "Bash finished"
  echo ""
) &

(
  time (
    for i in {1..10}
    do
      python factorial.py > /dev/null
    done
  )
  echo "Python finished"
  echo ""
) &

(
  time (
    for i in {1..10}
    do
      luajit factorial.lua > /dev/null
    done
  )
  echo "Luajit finished"
  echo ""
) &

(
  time (
    for i in {1..10}
    do
      node factorial.js > /dev/null
    done
  )
  echo "Node finished"
  echo ""
) &

wait

echo "All processes have finished!"
