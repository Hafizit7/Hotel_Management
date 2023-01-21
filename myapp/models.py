from django.db import models

# Create your models here.

class TeamMember(models.Model):
    image = models.ImageField(upload_to='ImageTeam')
    name = models.CharField(max_length = 150)
    roll = models.CharField(max_length = 150)
    shift = models.CharField(max_length = 150)

    class Meta:
        
        verbose_name = 'Team Meamber'
        verbose_name_plural = 'Team Meamber'

    def __str__(self):
        return self.name


class OurRoom(models.Model):
    Image = models.ImageField(upload_to='ImageRoom')
    Name = models.CharField(max_length = 150)
    Price = models.CharField(max_length = 150)
    discount_price = models.CharField(max_length = 150, blank=True, null=True)
    Day = models.CharField(max_length = 150)
    Room_Discription = models.CharField(max_length = 500)
    Distance = models.CharField(max_length = 150, blank=True, null=True)
    Catagory = models.CharField(max_length = 150, blank=True, null=True)
  
    class Meta:
    
        verbose_name = 'OurRoom'
        verbose_name_plural = 'OurRooms'

    def __str__(self):
        return self.Name


class RoomOrder(models.Model):
    full_name = models.CharField(max_length = 150)
    birthday = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 150)
    phone = models.CharField(max_length = 150)
    nid = models.CharField(max_length = 150)
    st_date = models.CharField(max_length = 150)
    end_date = models.CharField(max_length = 150)

    class Meta:
   
        verbose_name = 'RoomOrder'
        verbose_name_plural = 'RoomOrders'

    def __str__(self):
        return self.full_name
        


class Contact(models.Model):
    Name = models.CharField(max_length = 150)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length = 150)
    Massege = models.CharField(max_length = 150)

    class Meta:
      
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.Name



