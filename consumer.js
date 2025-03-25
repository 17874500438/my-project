// 消费者登录
$(document).on('click', '#consumer-login-btn', function () {
    const phoneNumber = $('#consumer-phone').val();
    const password = $('#consumer-password').val();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/consumer/login/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            phone_number: phoneNumber,
            password: password
        }),
        success: function (response) {
            if (response.status === 'success') {
                showPage('consumer-home');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 消费者注册
$(document).on('click', '#consumer-register-btn', function () {
    const phoneNumber = $('#consumer-register-phone').val();
    const password = $('#consumer-register-password').val();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/consumer/register/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            phone_number: phoneNumber,
            password: password
        }),
        success: function (response) {
            if (response.status === 'success') {
                alert('注册成功，请登录');
                showPage('consumer-login');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 消费者创建预约
$(document).on('click', '#consumer-create-appointment-btn', function () {
    const consumerId = $('#consumer-id').val();
    const barberId = $('#barber-id').val();
    const serviceId = $('#service-id').val();
    const appointmentTime = $('#appointment-time').val();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/appointments/create/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            consumer: consumerId,
            barber: barberId,
            service: serviceId,
            appointment_time: appointmentTime
        }),
        success: function (response) {
            if (response.status === 'success') {
                alert('预约创建成功');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 消费者提交反馈
$(document).on('click', '#consumer-submit-feedback-btn', function () {
    const consumerId = $('#consumer-id').val();
    const barberId = $('#barber-id').val();
    const rating = $('#rating').val();
    const content = $('#feedback-content').val();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/feedback/create/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            consumer: consumerId,
            barber: barberId,
            rating: rating,
            content: content
        }),
        success: function (response) {
            if (response.status === 'success') {
                alert('反馈提交成功');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});