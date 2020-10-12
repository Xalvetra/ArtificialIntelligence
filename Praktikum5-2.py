#!/usr/bin/env python
# coding: utf-8

# In[41]:


def makeTSP(nCities):
    position = 2*random.rand(nCities,2)-1;
    distances = zeros((nCities,nCities))
    
    for i in range(nCities):
        for j in range(i+1,nCities):
            distances[i,j] = sqrt((position[i,0]-position[j,0])**2 + (position[i,1] - position[j,1])**2);
        
    return distances    


# In[42]:


def permutation(order):
    order = tuple(order)
    if len(order)==1:
        yield order
    else:
        for i in range(len(order)):
            rest = order[:i] + order[i+1:]
            move = (order[i],)
            for smaller in permutation(rest):
                yield move+smaller


# In[43]:


def exhaustife(distances):
    nCities = shape(distances)[0]
    
    cityOrder = arange(nCities)
    
    distanceTravelled = 0
    for i in range(nCities-1):
        distanceTravelled +=[cityOrder[i], cityOrder[i+1]]
    possibleDistanceTravelled += distances[newOrder[nCities-1],0]
    
    if possibleDistanceTravelled < distanceTravelled:
        distanceTravelled = possibleDistanceTravelled
        cityOrder = newOrder
    return cityOrder, distanceTravelled


# In[44]:


def hillClimbing(distances):
    
    nCities = shape(distances)[0]
    
    cityOrder = arange(nCities)
    random.shuffle(cityOrder)
    
    distaceTravelled - 0
    for i in range(nCities-1):
        distanceTravelled += distaces[cityOrder[i],cityOrder[i+1]]
    distanceTravelled += distances[cityOrder[nCities-1],0]
    
    for i in range(1000):
        city1 = random.randint(nCities)
        city2 = random.randint(nCities)
        
        if city1 != city2:
            posibbleCityOrder = cityOrder.copy()
            posibbleCityOrder = where(possibleCityOrder==city1,-1,possibleCityOrder)
            posibbleCityOrder = where(possibleCityOrder==city2,city1,possibleCityOrder)
            posibbleCityOrder = where(possibleCityOrder==-1,city2,possibleCityOrder)
            
            newDistanceTravelled = 0
            for j in range(nCities-1):
                newDistanceTravelled += distances[possibleCityOrder[j],possibleCityOrder[j+1]]
            distanceTravelled += distances[cityOrder[nCities-1],0]
            
            if newDistanceTravelled < distanceTravelled:
                distanceTravelled = newDistanceTravelled
                cityOrder = possibleCityOrder
                
        return cityOrder, distanceTravelled


# In[47]:


def runAll():
    import time
    
    nCities = 5
    distances = makeTSP(nCities)

    print ("Exhaustive Search")
    start = time.time()
    print (exhaustive(distances))
    finish = time.time()
    print (finish-start)
    
    print("Hill Climbing")
    start = time.time()
    print (hillClimbing(distances))
    finish = time.time()
    print (finish-start)

    
    
runAll()


# In[ ]:




