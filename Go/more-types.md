## Structs

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
