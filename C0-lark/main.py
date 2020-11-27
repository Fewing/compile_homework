from lark import Lark

f_lark = open('test.lark')
lark = f_lark.read()
l = Lark(lark)
res = l.parse('''
fn fib(x: int) -> int {
    if x<=1 {
        return 1;
    }
    let result: int = fib(x - 1);
    result = result + fib(x - 2);
    return result;
}

fn main() -> int {
    let i: int = 0;
    let j: int;
    j = getint();
    while i < j {
        putint(i);
        putchar(32);
        putint(fib(i));
        putln();
        i = i + 1;
    }
    return 0;
}
''')
print(res.pretty())
