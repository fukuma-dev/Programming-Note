## Structs (構造体)

```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	fmt.Println(Vertex{1, 2})
}
```

### Result

```
{1 2}
```

構造体とはフィールドの集まりのこと

---

## 構造体の生成方法

構造体を生成するには大きく分けて2つの方法がある。
属性にXとYを持つ構造体を用意する。

```go
type Sample struct {
    X, Y int
}
```

### 1. new()を用いて生成する方法

```go
var s = new(Sample)
fmt.Println(s) // -> &{0,0}
```

* 属性は型毎に決められているゼロ値(intの場合は0)に設定される。
* 構造体のポインタ型が生成される

### 2. {}を用いて初期化する方法

```go
var s = Sample{X: 1, Y: 2}
fmt.Println(s) // -> {1,2}
```

---

## Struct Fields

```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v.X)
}
```

### Result

```
4
```

structのフィールドは，ドット( . )を用いてアクセスする。

---

## Pointers to structs

```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)
}
```

### Result
```
{1000000000 2}
```

structのフィールドは、structのポインタを通してアクセスすることもできる。

フィールド X を持つstructのポインタ p がある場合，フィールド X にアクセスするには (*p).X のように書くことができ流。
この表記は面倒なので，Goでは代わりに p.X と書くこともできる。
