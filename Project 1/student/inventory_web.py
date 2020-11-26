# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:00:02 2020

@author: krlig
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

CSCI204 Project 1 E-Commerce Inventory
Student Name: Kyle Light
Instructor Name: Professror Gutekunst
"""
import csv
import sys

class Inventory():
    
    def __init__(self):
        self.items=[]
        self.emarker=0
        self.fmarker=0
        self.hmarker=0
        Inventory.make_list(self)
        self.count=len(self.items)
        
        
    def check_type(self,obj): #checks to see what type of object the item is
        if isinstance(obj, Book)==True:
            return "Book"
        elif isinstance(obj,CD_Vinyl)==True:
            return "CD/Vinyl"
        elif isinstance(obj,Collectible)==True:
            return "Collectible"
        elif self.items.index(obj)<self.fmarker:
            return "electronics"
        elif self.items.index(obj)<self.hmarker:
            return "fashion"
        else:
            return "homegarden"

        
    def compute_inventory(self): #Finds total cost of inventory
        value=0
        for objects in self.items:
            value=value+(float(objects.price)*float(objects.quantity))
            
        return ("<p> The total cost of the inventory is: $"+str(value)+"</p>")
            
        
    def print_inventory(self,start=0,end=500):#prints defined section for the inventory
        
        if end==500:
            end=self.count
        
        s=''
        for i in range(start,end):
            s=s+"<p> ID: "+str(i)+"</p>"
            s=s+"<p>"+str(self.items[i])+"</p>"
           
        print("S value:"+s)
        return s
        
        
    def print_category(self,title): #prints categroies of a specific item type
        newtitle=title.lower()
        
        for item in self.items:
            if newtitle=='book':
                if isinstance(item,Book)==True:
                    print ("ID: "+str(self.items.index(item)))
                    print(item)
            
            elif newtitle=='cd_vinyl':
                if isinstance(item,CD_Vinyl)==True:
                    print ("ID: "+str(self.items.index(item)))
                    print(item)
                    
            elif newtitle=='collectible':
                if isinstance(item,Collectible)==True:
                    print ("ID: "+str(self.items.index(item)))
                    print(item)
                    
            elif newtitle=='electronics':
                if self.items.index(item)<self.fmarker and self.items.index(item)>=self.emarker:
                    print ("ID: "+str(self.items.index(item)))
                    print(item)
            
            elif newtitle=='fashion':
                if self.items.index(item)<self.hmarker and self.items.index(item)>=self.fmarker:
                    print ("ID: "+str(self.items.index(item)))
                    print(item)
            
            elif newtitle=='homegarden':
                if self.items.index(item)>=self.hmarker:
                    print ("ID: "+str(self.items.index(item)))
                    print(item)
            else:
                print("Item category not found")
            
                
    def search_item(self,phrase):#finds items based on the sent in phrase
        s=''
        for item in self.items:
            newname=item.name.lower()
            if newname.find(phrase)!=-1:
                s=s+"<p> ID: "+str(self.items.index(item))+"</p>"
                s=s+"<p>"+str(item)+"</p>"
                
        return s
            
        
    def make_list(self): #creates one list of various class objects by converting CSV files
        file_list=['book.csv', 'cd_vinyl.csv', 'collectible.csv', 'electronics.csv', 'fashion.csv', 'home_garden.csv' ]
        
        for words in file_list:
            
            with open(words, newline='') as f:
                reader = csv.reader(f)
                your_list = list(reader)

            skip=0
            for lists in your_list:
                if skip==0:
                    skip=0 #basically do nothing in order to skip all the titles at the beginning of the csv files
                elif file_list.index(words)==0:
                    obj=Book(lists[0],lists[4],lists[1],lists[6],lists[3],lists[2],lists[5])
                    self.items.append(obj)
                elif file_list.index(words)==1:
                    obj=CD_Vinyl(lists[0],lists[5],lists[4],lists[6],lists[1],lists[2],lists[3])
                    self.items.append(obj)
                elif file_list.index(words)==2:
                    obj=Collectible(lists[0],lists[1],lists[2],lists[3],lists[4])
                    self.items.append(obj)
                else:
                    obj=Item(lists[0],lists[1],lists[2],lists[3],lists[4])
                    self.items.append(obj)
                    
                    if skip==1: #set markers for where each subsection of Item begins in the list
                        if self.emarker==0:
                            self.emarker=len(self.items)-1
                        elif self.fmarker==0:
                            self.fmarker=len(self.items)-1
                        elif self.hmarker==0:
                            self.hmarker=len(self.items)-1
                skip+=1
                    
        
        
class Item():
    
    def __init__(self,name,price,date,manufacturer,quantity):
        self.name=name
        self.price=price
        self.date=date
        self.manufacturer=manufacturer
        self.quantity=quantity
        
    def __str__(self,title="Manufacturer"):
        return "Name: "+self.name+'\n'+"Price: $"+self.price+'\n'+"Date: "+self.date+'\n'+"Quantity: "+self.quantity+'\n'+title+": "+self.manufacturer+'\n'
    
    
class Book(Item):
    
    def __init__(self,name,price,date,quantity,author,publish, ISBN):
        super().__init__(name,price,date,author,quantity)
        self.publish=publish
        self.ISBN=ISBN
        
    def __str__(self):
        return super().__str__("Author: ") +"Publish: "+ self.publish +'\n'+"ISBN: "+self.ISBN+'\n'
    
    
class CD_Vinyl(Item):
    
    def __init__(self,name,price,date,quantity,artist,label, ASIN):
        super().__init__(name,price,date,artist,quantity)
        self.artist=artist
        self.ASIN=ASIN
        self.label=label
        
    def __str__(self):
        return super().__str__("Artist: ")+ "Label: "+self.label+'\n'+"ASIN: "+self.ASIN+'\n'
    
    
class Collectible(Item):
    
    def __init__(self,name,price,date,owner,quantity):
        super().__init__(name,price,date,owner,quantity)
        
    def __str__(self):
        return super().__str__("Owner: ")