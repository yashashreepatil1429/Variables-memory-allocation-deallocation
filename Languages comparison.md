# JavaScript, Python, Node.js, and Java: Variables, Memory, and Runtime

This guide compares JavaScript, Python, and Java, with Node.js included as a
JavaScript runtime environment. Node.js is not a separate programming language:
it runs JavaScript (commonly using the V8 engine) and adds APIs for servers,
files, networking, and other system tasks.

Some implementation details depend on the runtime and version. Python examples
below generally describe CPython, the most common Python implementation; Java
examples describe a typical JVM; and Node.js examples generally describe V8.
Language-level behavior is distinguished from implementation details where
that distinction matters.

## 1. Variable declaration

| Language | How a name is introduced | What the declaration means |
| --- | --- | --- |
| JavaScript | `let`, `const`, or `var` | `let` and `const` are block-scoped. `const` prevents rebinding the name, but does not make an object immutable. `var` is function-scoped (or global-scoped) and has older hoisting behavior. Prefer `const` by default and `let` when reassignment is needed. |
| Python | Assignment, such as `count = 3` | Assignment binds a name to an object. A separate declaration keyword is not normally needed. Scope is determined by where the name is bound and Python's scope rules. |
| Java | A type and a name, such as `int count = 3;` | A local variable has a declared type, and the compiler checks assignments and uses against that type. Fields and local variables have different default-initialization rules; local variables must be definitely assigned before use. |

```javascript
const user = { name: "Ari" };
user.name = "Bo";       // allowed: the object can still be changed
// user = {};           // TypeError: the const binding cannot be reassigned
```

```python
user = {"name": "Ari"}
user = {"name": "Bo"}   # allowed: the name is rebound
```

```java
String user = "Ari";
user = "Bo";            // allowed: the variable is not final
```

## 2. Static and dynamic typing

- **Java is statically typed.** Types are checked primarily at compile time.
  Runtime checks still exist, for example casts, array-store checks, and null
  dereferences.
- **JavaScript and Python are dynamically typed.** A value has a type at
  runtime, and a name can be rebound to values of different types. Operations
  are checked as the program runs.
- This is about when and how type rules are checked, not whether a language has
  types. JavaScript and Python both have types.

```javascript
let value = 10;
value = "ten";          // legal; value now refers to a string
```

```python
value = 10
value = "ten"           # legal; value now refers to a string
```

```java
int value = 10;
// value = "ten";       // compile-time error
```

Dynamic typing can make experimentation concise, but a type error may be
discovered only when the affected execution path runs. Static typing catches
many incompatible operations earlier, but does not prove a program is free of
all runtime errors.

## 3. Primitive and reference/object types

- **JavaScript** has primitive values: `undefined`, `null`, booleans, numbers,
  bigints, strings, and symbols. Objects include arrays, functions, and plain
  objects. Primitives are immutable values; objects are mutable unless
  constrained by program logic or APIs.
- **Python** treats values, including integers and strings, as objects. Names
  refer to objects. Some objects are immutable (such as `int`, `str`, and
  `tuple`); others are mutable (such as `list`, `dict`, and most user-defined
  instances).
- **Java** distinguishes primitive types such as `int` and `boolean` from
  reference types such as `String`, arrays, and class instances. A reference
  variable can contain `null`. Java generics use reference types, so primitive
  values may be boxed, for example `int` to `Integer`.

These differences affect representation and operations, but do not mean that
every primitive is physically stored on a stack or every object is physically
stored on a heap. Storage and optimization are implementation concerns (see
section 6).

## 4. Names, objects, and assignment

A useful mental model is **name/variable -> value**. For reference-like values,
that value identifies or refers to an object. Assignment usually binds or copies
the value; it does not automatically clone the object.

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3] -- both names refer to the same list
```

```javascript
const a = { score: 1 };
const b = a;
b.score = 2;
console.log(a.score); // 2 -- both bindings refer to the same object
```

In Java, assigning an object variable copies the reference value:

```java
int[] a = {1, 2};
int[] b = a;
b[0] = 9;
System.out.println(a[0]); // 9 -- both references point to the same array
```

To make an independent object, use an appropriate copy operation. A shallow
copy duplicates only the outer container; nested objects may remain shared. A
deep copy recursively duplicates nested content, but its meaning depends on the
types involved.

Primitive assignment in Java copies the primitive value. JavaScript primitive
values and Python immutable values also cannot be changed through an alias;
reassignment makes a name refer to another value rather than modifying the
original value.

## 5. Mutable and immutable values

**Mutable** objects can be changed in place. **Immutable** values cannot; an
operation that appears to modify one instead produces another value.

| Example | JavaScript | Python | Java |
| --- | --- | --- | --- |
| Text | Strings are immutable. | Strings are immutable. | `String` is immutable. |
| List-like collection | Arrays are mutable. | Lists are mutable. | Arrays are mutable; collections such as `ArrayList` are mutable. |
| Object/instance | Plain objects are usually mutable. | Most user-defined instances are mutable unless designed otherwise. | Most class instances are mutable unless designed otherwise. |

```javascript
let text = "cat";
text.toUpperCase();       // returns "CAT"; it does not change text
text = text.toUpperCase();

const items = [1, 2];
items.push(3);            // changes the existing array
```

```python
text = "cat"
text.upper()              # returns "CAT"; text is still "cat"
text = text.upper()

items = [1, 2]
items.append(3)           # changes the existing list
```

```java
String text = "cat";
text.toUpperCase();       // returns "CAT"; text is still "cat"
text = text.toUpperCase();

int[] items = {1, 2};
items[0] = 9;             // changes the existing array
```

The word `const` in JavaScript applies to the binding, not the mutability of
the referenced object. Java's `final` has the same important distinction for
references: a `final` reference cannot be reassigned, but the referenced object
may still be mutable.

## 6. Memory: stack and heap

- A **call stack** tracks active function or method calls. A typical call frame
  contains bookkeeping such as the return location and information needed for
  parameters and local execution state.
- The **heap** is a common area for dynamically managed objects and data whose
  lifetime is not limited to one call.
- These are useful conceptual regions, not a complete map of every runtime's
  memory.

The shortcut **"variables are on the stack, objects are on the heap" is
incomplete**:

1. A local variable may hold a primitive value, a reference, or a value that
   the runtime/compiler represents in another way.
2. A reference may be in a stack frame while the object it refers to is on the
   heap.
3. Objects can outlive the function that created them when something else
   retains a reference to them.
4. Compilers and virtual machines can optimize storage, eliminate allocations,
   or keep values in registers. The source language usually does not promise a
   specific physical layout.
5. In Python, names refer to objects, but the exact representation and memory
   placement are implementation details.

Think in terms of **scope, reachability, and lifetime** first. Use stack/heap
as a high-level model, not a guaranteed per-variable placement rule.

## 7. Function and method memory

When a function or method is called, the runtime tracks a new active call. The
call has parameters and local execution state. When it returns, that call is no
longer active and its frame can be discarded. A returned object can remain
alive if the caller or another part of the program retains it.

```python
def make_pair(value):
    local = [value, value + 1]
    return local

pair = make_pair(4)  # the call has returned, but pair keeps the list reachable
```

The returned value is not necessarily copied. In this example, the returned
value is a reference to the list. A return value may instead be a primitive or
immutable value, depending on the language and expression.

Recursion creates multiple active calls, each with its own logical call state.
Very deep recursion can exhaust the call stack or hit a language/runtime limit.

## 8. Functions across the languages

- **JavaScript and Python** treat functions as first-class values: they can be
  assigned to variables, passed to other functions, and returned.
- **Java** has methods associated with classes or objects. Since Java 8,
  lambdas and method references can be used where a functional interface (an
  interface with one abstract method) is expected. A lambda is not a free-
  standing method declaration, although it can be passed and stored through
  that interface.

```javascript
function applyTwice(fn, value) {
  return fn(fn(value));
}
const result = applyTwice(x => x + 1, 3); // 5
```

```python
def apply_twice(fn, value):
    return fn(fn(value))

result = apply_twice(lambda x: x + 1, 3)  # 5
```

```java
import java.util.function.UnaryOperator;

static int applyTwice(UnaryOperator<Integer> fn, int value) {
    return fn.apply(fn.apply(value));
}

int result = applyTwice(x -> x + 1, 3); // 5
```

## 9. Pass-by-value and references

The key distinction is between **passing a value** and **mutating the object
that value refers to**.

- Java is pass-by-value. For an object argument, the copied value is the
  reference. The method can mutate the shared object, but reassigning its local
  parameter does not reassign the caller's variable.
- JavaScript passes argument values. For an object, the value identifies the
  object, so the function can mutate the shared object. Reassigning the
  parameter does not change the caller's binding.
- Python's argument passing is often described as "call by sharing" or
  "object-reference passing": the parameter is bound to the same object as the
  argument. Mutations to a mutable object are visible to the caller, but
  rebinding the local parameter is not.

```java
static void change(int[] values) {
    values[0] = 7;           // visible to caller
    values = new int[]{9};   // only rebinds the local parameter
}
```

```javascript
function change(values) {
  values[0] = 7;             // visible to caller
  values = [9];              // only rebinds the local parameter
}
```

```python
def change(values):
    values[0] = 7            # visible to caller
    values = [9]              # only rebinds the local parameter
```

In all three examples, the caller's original array/list still has its first
element changed to `7`; it is not replaced with `[9]`. Java primitive arguments
and JavaScript primitive arguments also pass their values, so assigning a new
value to a parameter does not change the caller's variable.

## 10. Closures and captured variables

A **closure** is a function together with access to variables from its
surrounding lexical scope. Captured state can remain available after the outer
function returns because the returned function (or another retained object)
keeps that state reachable.

```javascript
function makeCounter() {
  let count = 0;
  return () => ++count;
}
const next = makeCounter();
next(); // 1
next(); // 2
```

```python
def make_counter():
    count = 0

    def next_value():
        nonlocal count
        count += 1
        return count

    return next_value

next_value = make_counter()
next_value()  # 1
next_value()  # 2
```

Java lambdas can capture local variables only when they are `final` or
**effectively final** (not reassigned after initialization). The captured local
value is retained for use by the lambda; Java does not allow a lambda to
reassign the enclosing local variable. If the captured value is a reference to
a mutable object, the lambda may still mutate that object.

Captured state can extend an object's lifetime. A closure retained by a global
variable, event listener, or long-running task may keep otherwise-unneeded
objects reachable.

## 11. Garbage collection and object lifetime

Garbage collection (GC) reclaims memory used by objects that the runtime
considers no longer needed. It reduces the need for programmers to manually
free every object, but it does not make memory management irrelevant.

- An object is generally **eligible for collection** when it is no longer
  reachable through references the runtime treats as live.
- Eligibility does not mean collection happens immediately. A collector may
  run later, and the runtime may retain freed memory for reuse rather than
  returning it to the operating system immediately.
- JavaScript's `delete` removes an object property; it does not directly free
  the object.
- Python's `del` removes a name, item, or attribute binding; it does not
  guarantee immediate memory release. In CPython, removing the last reference
  often decreases the reference count to zero, but cycles and implementation
  details affect reclamation.

Resource cleanup is separate from ordinary object memory collection. Files,
sockets, database connections, and locks should be closed or released using
language/runtime mechanisms such as Python context managers, Java
try-with-resources, or explicit Node.js stream/resource cleanup.

## 12. Garbage collection comparison

- **JavaScript in V8 / Node.js:** uses a tracing garbage collector. It starts
  from roots such as active execution state and globals, then identifies
  reachable objects. Collection timing is not deterministic.
- **CPython:** primarily uses reference counting, supplemented by a cyclic
  garbage collector to find certain unreachable reference cycles. Other Python
  implementations may manage memory differently.
- **Java on the JVM:** uses tracing garbage collection. The JVM provides
  different collectors and tuning options; exact algorithms and timing depend
  on the JVM and configuration.

Do not rely on a particular collection time for program correctness.

## 13. Memory leaks despite garbage collection

A garbage collector cannot reclaim an object that is still reachable, even if
the program no longer needs it. This is commonly called a **memory leak** at
the application level.

Common causes include:

- unbounded caches or collections;
- references accidentally stored in globals or long-lived objects;
- event listeners, callbacks, or timers that are never removed;
- retaining request data after a request completes;
- closures that keep large objects alive;
- queues that are produced into faster than they are consumed.

The fix is usually to correct ownership and lifetime: remove listeners, bound
caches, clear completed work, or avoid retaining data unnecessarily. Calling
GC manually is rarely a substitute for removing unwanted references.

## 14. Runtime comparison

- **JavaScript** is the language. It can run in browsers and other environments.
- **V8** is Google's JavaScript engine. Node.js commonly embeds V8 to execute
  JavaScript.
- **Node.js** is a runtime environment around JavaScript. It provides APIs and
  libraries for processes, files, networking, and servers. Its event-driven
  I/O stack uses components including `libuv`.
- **Python** is the language; **CPython** is its most widely used
  implementation. Python also has other implementations with different
  internals.
- **Java** source is generally compiled to JVM bytecode, which runs on a Java
  Virtual Machine (JVM). Different vendors provide JVM implementations.

Thus, comparing "Node.js versus Python versus Java" mixes a runtime environment,
a language/implementation pairing, and a language plus virtual machine. For a
fair comparison, specify the implementation and workload, for example
"Node.js on V8 versus CPython versus OpenJDK HotSpot."

## 15. Compilation, interpretation, and JIT

The simple split **"compiled versus interpreted"** is misleading because modern
language implementations commonly combine techniques.

- **JavaScript/V8:** parses and executes code, and may compile frequently used
  code to optimized machine code. It can de-optimize code if assumptions stop
  holding.
- **CPython:** typically compiles source to Python bytecode, then executes that
  bytecode in its virtual machine. This is different from compiling the whole
  program directly to native machine code. Other Python implementations can
  use different strategies.
- **Java/JVM:** `javac` commonly compiles Java source into bytecode. The JVM
  interprets bytecode and may JIT-compile hot paths into native machine code.

Compilation strategy affects startup, warm-up, optimization, debugging, and
deployment. It does not by itself determine which program is faster.

## 16. Event loops, asynchronous I/O, and threads

- **Node.js:** JavaScript callbacks and promise continuations are scheduled
  through an event loop. Non-blocking I/O lets one JavaScript thread handle
  many waiting operations. Some work is performed by the operating system or
  `libuv`'s worker pool. Long CPU-bound JavaScript blocks that event loop unless
  work is moved to worker threads or another process.
- **Python:** `asyncio` provides event-loop-based asynchronous I/O. In standard
  CPython builds, the Global Interpreter Lock (GIL) generally limits parallel
  execution of Python bytecode across threads, though threads remain useful for
  I/O-bound work and native extensions may release the GIL. Processes can
  provide parallel CPU execution.
- **Java:** supports threads and multiple concurrency APIs. Threads can run
  CPU work in parallel, subject to available cores and synchronization costs.
  Java also supports asynchronous and non-blocking I/O.

For **I/O-bound** work, asynchronous I/O or threads can keep work progressing
while waiting on files, networks, or databases. For **CPU-bound** work, use
parallel execution appropriate to the runtime, and measure synchronization,
serialization, and scheduling overhead.

## 17. A real HTTP request flow

A typical server request follows this path:

1. A runtime or web framework receives an HTTP request.
2. Routing selects a handler function or method.
3. The handler reads request data and binds names to values or objects.
4. Validation and business logic run.
5. The handler may call a database or another API, often waiting for I/O.
6. Results are converted into a response body and status code.
7. The runtime/framework sends the response and releases request-specific
   references when they are no longer needed.

The same broad steps apply in Node.js, Python web frameworks, and Java web
frameworks. Their APIs and concurrency models differ. A request's local
variables normally stop being needed when its handler finishes, but data
retained in caches, background jobs, global state, or callbacks may live longer.

## 18. Performance

There is no useful universal answer to **"Which language is fastest?"**
Performance depends on:

- the workload (CPU-bound, I/O-bound, latency-sensitive, or throughput-heavy);
- algorithms and data structures;
- runtime, engine/JVM version, and warm-up;
- memory allocation and garbage-collection behavior;
- database, network, and filesystem time;
- concurrency design and deployment configuration.

Measure the actual application with representative data. Profile before
optimizing, and distinguish time spent in application code from time spent
waiting on external systems.

## 19. Memory lifetime: name, object, and collection

It helps to separate three questions:

1. **How long does a name exist?** This is controlled by scope and execution.
   A local name is normally usable only while its scope is active, though
   closures or runtime details can extend the lifetime of associated state.
2. **How long does an object remain reachable?** It remains reachable while
   some live reference path leads to it, such as from a local variable, a
   global, another object, or a closure.
3. **When is its memory reclaimed?** Once unreachable, an object may be
   eligible for collection, but reclamation time and returning memory to the
   operating system are runtime-dependent.

These timelines are related but not identical. A name can go out of scope while
an object remains reachable elsewhere; an object can be unreachable before the
runtime actually reclaims its memory.

## 20. What happens when `result = a + b` executes?

The exact work depends on the types and runtime. In general, the program
evaluates `a` and `b`, applies the language's addition rules, obtains a result,
then binds or stores that result under `result`.

### Python

```python
result = a + b
```

Python looks up the names `a` and `b`, then applies the `+` operation supported
by their runtime objects (commonly through methods such as `__add__`, with
additional rules for reflected operations). For integers, it computes an
integer result; for strings, `+` concatenates strings; incompatible operands
may raise `TypeError`. The name `result` is then bound to the returned value.
In CPython, the operation is executed through Python bytecode and runtime
machinery, but the language does not require a particular memory layout for
these names or values.

### JavaScript

```javascript
const result = a + b;
```

JavaScript evaluates both expressions and applies the `+` operator's rules.
Depending on the operand types, `+` can perform numeric addition or string
concatenation; objects may be converted to primitives first. For example,
`2 + 3` is `5`, while `"2" + 3` is `"23"`. The resulting value is bound to
`result`; `const` prevents rebinding that name. If `a` or `b` is not defined in
the relevant scope, evaluation throws a `ReferenceError`.

### Java

```java
int result = a + b;
```

The compiler checks that `a` and `b` are declared and that their types support
the operation. If both are `int`, the JVM performs integer addition and stores
the result in the local variable `result` (subject to implementation
optimizations). Java integer overflow wraps according to the fixed-width
integer rules; it does not automatically raise an overflow exception. If the
operands are references such as `String`, the applicable `+` operation may
instead concatenate strings, but the destination type must match the result.

The visible line is short, but it involves name lookup, type/operator rules,
computation, and a binding or storage operation. Runtime dispatch, conversion,
allocation, and optimization depend on the operands and implementation.
