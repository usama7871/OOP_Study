# 🎸 OOP Study: The Rock Star's Guide to Object-Oriented Programming 🎸

[![GitHub](https://img.shields.io/badge/GitHub-OOP__Study-blue?style=for-the-badge&logo=github)](https://github.com/usama7871/OOP_Study)
[![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Paradigm-OOP-red?style=for-the-badge&logo=python)](https://en.wikipedia.org/wiki/Object-oriented_programming)

## 🤘 Introduction

Welcome to the **OOP Study** repository - where we turn Object-Oriented Programming from cryptic code into a rock concert of clarity! This project is a collection of 21 assignments designed to master Python OOP concepts from basic to advanced levels.

> "Learn OOP like you'd learn a guitar: practice the fundamentals until they become second nature, then rock the world with your creativity!" 🎵

## 🔥 Project Structure

This repo is organized like a greatest hits album - each track (assignment) covers a specific OOP concept:

```
OOP_Study/
├── 01_self.py/
├── 02_cls.py/
├── 03_public_variables.py/
├── 04_class_variables.py/
├── ...
└── 21_custom_iterable.py/
```

## 📋 Assignment Breakdown

### 1. 🎵 Using `self` - The Lead Singer

**Assignment:** Create a `Student` class with attributes and methods that use `self` for object identity.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")
```

### 2. 🥁 Using `cls` - The Rhythm Keeper

**Assignment:** Create a `Counter` class that tracks how many instances have been created.

### 3. 🎸 Public Variables and Methods - Playing for Everyone

**Assignment:** Create a `Car` class with public variables and methods that can be accessed from anywhere.

### 4. 🎹 Class Variables and Methods - The Keyboard Binding It All

**Assignment:** Create a `Bank` class with shared variables across all instances.

### 5. 🎺 Static Variables and Methods - The Brass Section

**Assignment:** Create a `MathUtils` class with utility methods that don't require instance state.

### 6. 🎭 Constructors and Destructors - The Opening and Closing Acts

**Assignment:** Create a `Logger` class that announces its birth and death.

### 7. 🔒 Access Modifiers - The Backstage Passes

**Assignment:** Create an `Employee` class with different levels of access control.

### 8. 👑 The `super()` Function - Standing on the Shoulders of Legends

**Assignment:** Use inheritance with `super()` to extend functionality.

### 9. 🧩 Abstract Classes and Methods - The Musical Score

**Assignment:** Create an abstract `Shape` class that defines an interface for concrete classes.

### 10. 🐕 Instance Methods - Each Band Member's Solo

**Assignment:** Create instance methods that operate on object state.

### 11. 📚 Class Methods - The Band's Shared History

**Assignment:** Track shared state with class methods.

### 12. 🌡️ Static Methods - The Roadie's Toolbox

**Assignment:** Create utility methods that don't depend on class or instance state.

### 13. 🏎️ Composition - Putting the Band Together

**Assignment:** Create complex objects by combining simpler ones.

### 14. 🏢 Aggregation - The Concert Venue

**Assignment:** Use loose coupling between objects.

### 15. 💎 Method Resolution Order - The Encore Decision

**Assignment:** Navigate complex inheritance hierarchies.

### 16. ✨ Function Decorators - The Sound Effects

**Assignment:** Enhance functions with additional behavior.

### 17. 🎁 Class Decorators - The Makeover

**Assignment:** Transform entire classes with decorators.

### 18. 🏷️ Property Decorators - The Mixing Board

**Assignment:** Control access to class attributes.

### 19. 📞 `callable()` and `__call__()` - The Hotline

**Assignment:** Make objects that can be called like functions.

### 20. ⚠️ Custom Exceptions - The Security Team

**Assignment:** Create specialized error types.

### 21. 🔄 Custom Iterables - The Playlist

**Assignment:** Make classes that can be used in loops.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Basic understanding of programming concepts
- A desire to rock the world of OOP! 🤘

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/usama7871/OOP_Study.git
   cd OOP_Study
   ```

2. Explore the directories for each concept

3. Run the examples:
   ```bash
   python 01_self_keyword/student.py
   ```

## 🎵 The OOP Journey: A Rock Epic

Picture yourself as a rookie guitarist picking up your first instrument. That's where we all start with programming - simple functions, basic syntax.

But true rock stars know there's more to music than individual notes - there's harmony, composition, and style. That's what Object-Oriented Programming brings to code!

In this repo, we start with the basics (`self`, public variables) and build up to complex compositions (inheritance hierarchies, decorators, custom iterables). With each assignment, you'll add another technique to your coding repertoire.

By the end, you won't just be playing cover songs - you'll be composing your own programming symphonies!

## 📝 Usage Examples

### Example 1: Creating a Student

```python
from student import Student

# Create a new student
alice = Student("Alice Cooper", 95)

# Display student details
alice.display()  # Student Name: Alice Cooper, Marks: 95
```

### Example 2: Working with a Counter

```python
from counter import Counter

# Create counter objects
c1 = Counter()
c2 = Counter()

# Display count
print(Counter.get_count())  # 2
```

## 🤝 Contributing

Rock stars inspire each other! Feel free to contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is available for educational purposes - rock on and learn!

## 🌟 Acknowledgements

- Inspired by the need to make OOP concepts crystal clear
- Shout out to all programming educators who make learning a blast
- Special thanks to the Python community for keeping the language evolving

---

🎤 **"Code is like rock and roll - it's not about the notes you play, it's about the notes you don't play."** - OOP Philosopher 🎤
