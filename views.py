from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Consumer, Barber, Service, HaircutOrder, Feedback, Leave
from .serializers import ConsumerSerializer, BarberSerializer, ServiceSerializer, HaircutOrderSerializer, FeedbackSerializer, LeaveSerializer
from django.contrib.auth.hashers import make_password, check_password

# 消费者注册
class ConsumerRegisterView(APIView):
    def post(self, request):
        serializer = ConsumerSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            serializer.validated_data['password'] = make_password(password)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 消费者登录
class ConsumerLoginView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        try:
            consumer = Consumer.objects.get(phone_number=phone_number)
            if check_password(password, consumer.password):
                serializer = ConsumerSerializer(consumer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': '密码错误'}, status=status.HTTP_401_UNAUTHORIZED)
        except Consumer.DoesNotExist:
            return Response({'error': '用户不存在'}, status=status.HTTP_401_UNAUTHORIZED)

# 理发师登录
class BarberLoginView(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        try:
            barber = Barber.objects.get(account=account)
            if check_password(password, barber.password):
                serializer = BarberSerializer(barber)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': '密码错误'}, status=status.HTTP_401_UNAUTHORIZED)
        except Barber.DoesNotExist:
            return Response({'error': '用户不存在'}, status=status.HTTP_401_UNAUTHORIZED)

# 管理员登录（简单模拟）
class AdminLoginView(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        if account == 'admin' and password == 'admin123':
            return Response({'message': '登录成功'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': '用户名或密码错误'}, status=status.HTTP_401_UNAUTHORIZED)

# 获取服务项目列表
class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 创建预约
class AppointmentCreateView(APIView):
    def post(self, request):
        serializer = HaircutOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 获取理发师的预约列表
class BarberAppointmentListView(APIView):
    def get(self, request, barber_id):
        appointments = HaircutOrder.objects.filter(barber_id=barber_id)
        serializer = HaircutOrderSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 理发师审核预约
class BarberAppointmentApproveView(APIView):
    def post(self, request, appointment_id):
        try:
            appointment = HaircutOrder.objects.get(id=appointment_id)
            is_approved = request.data.get('is_approved')
            appointment.is_approved = is_approved
            appointment.save()
            serializer = HaircutOrderSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except HaircutOrder.DoesNotExist:
            return Response({'error': '预约不存在'}, status=status.HTTP_404_NOT_FOUND)

# 消费者到店核销
class ConsumerArrivalView(APIView):
    def post(self, request, appointment_id):
        try:
            appointment = HaircutOrder.objects.get(id=appointment_id)
            appointment.is_arrived = True
            appointment.save()
            serializer = HaircutOrderSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except HaircutOrder.DoesNotExist:
            return Response({'error': '预约不存在'}, status=status.HTTP_404_NOT_FOUND)

# 提交反馈
class FeedbackCreateView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 理发师请假申请
class LeaveCreateView(APIView):
    def post(self, request):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 管理员获取请假申请列表
class AdminLeaveListView(APIView):
    def get(self, request):
        leaves = Leave.objects.all()
        serializer = LeaveSerializer(leaves, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 管理员审批请假申请
class AdminLeaveApproveView(APIView):
    def post(self, request, leave_id):
        try:
            leave = Leave.objects.get(id=leave_id)
            is_approved = request.data.get('is_approved')
            leave.is_approved = is_approved
            leave.save()
            serializer = LeaveSerializer(leave)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Leave.DoesNotExist:
            return Response({'error': '请假申请不存在'}, status=status.HTTP_404_NOT_FOUND)

# 管理员获取反馈列表
class AdminFeedbackListView(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 管理员处理反馈（简单模拟回复）
class AdminFeedbackHandleView(APIView):
    def post(self, request, feedback_id):
        try:
            feedback = Feedback.objects.get(id=feedback_id)
            # 这里可以添加实际的回复逻辑
            return Response({'message': '反馈已处理'}, status=status.HTTP_200_OK)
        except Feedback.DoesNotExist:
            return Response({'error': '反馈不存在'}, status=status.HTTP_404_NOT_FOUND)

# 管理员获取预约异常列表（简单模拟）
class AdminAppointmentExceptionListView(APIView):
    def get(self, request):
        appointments = HaircutOrder.objects.filter(is_approved=False)
        serializer = HaircutOrderSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 管理员处理预约异常（简单模拟）
class AdminAppointmentExceptionHandleView(APIView):
    def post(self, request, appointment_id):
        try:
            appointment = HaircutOrder.objects.get(id=appointment_id)
            # 这里可以添加实际的处理逻辑
            return Response({'message': '预约异常已处理'}, status=status.HTTP_200_OK)
        except HaircutOrder.DoesNotExist:
            return Response({'error': '预约不存在'}, status=status.HTTP_404_NOT_FOUND)

# 管理员获取会员申请列表（简单模拟）
class AdminMemberApplyListView(APIView):
    def get(self, request):
        consumers = Consumer.objects.filter(total_consumption__gte=1000, is_member=False)  # 假设消费满 1000 可申请会员
        serializer = ConsumerSerializer(consumers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 管理员审批会员申请
class AdminMemberApplyApproveView(APIView):
    def post(self, request, consumer_id):
        try:
            consumer = Consumer.objects.get(id=consumer_id)
            is_approved = request.data.get('is_approved')
            if is_approved:
                consumer.is_member = True
                consumer.save()
            return Response({'message': '会员申请已处理'}, status=status.HTTP_200_OK)
        except Consumer.DoesNotExist:
            return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)

# 管理员获取理发师晋升列表（简单模拟）
class AdminBarberPromotionListView(APIView):
    def get(self, request):
        barbers = Barber.objects.all()
        serializer = BarberSerializer(barbers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 管理员处理理发师晋升（简单模拟）
class AdminBarberPromotionHandleView(APIView):
    def post(self, request, barber_id):
        try:
            barber = Barber.objects.get(id=barber_id)
            # 这里可以添加实际的晋升逻辑
            return Response({'message': '理发师晋升已处理'}, status=status.HTTP_200_OK)
        except Barber.DoesNotExist:
            return Response({'error': '理发师不存在'}, status=status.HTTP_404_NOT_FOUND)