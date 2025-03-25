from django.db import models

# 消费者模型
class Consumer(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=128)
    is_member = models.BooleanField(default=False)
    total_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.phone_number

# 理发师模型
class Barber(models.Model):
    account = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.account

# 服务项目模型（原发型表）
class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# 订单模型，修改类名并指定表名
class HaircutOrder(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    is_arrived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.consumer} - {self.barber} - {self.appointment_time}"

    class Meta:
        db_table = 'haircutorder'

# 反馈模型
class Feedback(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.consumer} - {self.barber} - {self.rating}"

# 请假模型
class Leave(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.barber} - {self.start_time} - {self.end_time}"