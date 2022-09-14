# Worker HashTab
Project made in the 4th period of college, on Data Structure subject. The objective was create an algorithm for store and manage basic datas of workers in a company, applying the hashtab data structure.


Generate Key:
```
def hashing(self, name):
    return ord(name[0]) % self.size
```

HashTab before insertion:
Key 0 | Key 1 | Key 2 | Key 3 | Key 4 | Key 5 | Key 6 | Key 7 | Key 8 | Key 9
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
None | None | None | None | None | None | None | None | None | None  

HashTab after insertion:
Key 0 | Key 1 | Key 2 | Key 3 | Key 4 | Key 5 | Key 6 | Key 7 | Key 8 | Key 9
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
Name: Mike, Wage: $ 1000 | Name: John, Wage: $ 800 | Name: Ruty, Wage: $ 450 | Name: Lilly, Wage: $ 690 | Name: Margot, Wage: $ 2500 | Name: Bruce, Wage: $ 500 | Name: Malone, Wage: $ 300 | Name: Mary, Wage: $ 300 | Name: Otis, Wage: $ 700 | Name: Mavie, Wage: $ 300  
None | None | None | None | None | None | None | None | None | None  
