
## Defer

```go
package main

import "fmt"

func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}
```

### Result
```
hello
world

Program exited.
```

* deferは関数の実行を遅延させるステートメント
* 呼び出した関数内でreturnされるときに実行される
* deferへ渡した関数の引数はすぐに評価されるが，その関数自体は呼び出し元の関数がreturnするまで実行されない。


## Stacking defers

```go
package main

import "fmt"

func main() {
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}

	fmt.Println("done")
}
```

### Result
```
counting
done
9
8
7
6
5
4
3
2
1
0
```

* deferへ渡した関数が複数ある場合，その呼び出しはスタック(stack)される。
* 呼び出し元の関数がreturnするとき，deferへ渡した関数はLIFO(last-in-first-out) の順番で実行される。
