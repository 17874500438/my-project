// 理发师登录
$(document).on('click', '#barber-login-submit-btn', function () {
    const account = $('#barber-account').val();
    const password = $('#barber-password').val();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/barber/login/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            account: account,
            password: password
        }),
        success: function (response) {
            if (response.status === 'success') {
                showPage('barber-home');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 理发师获取预约列表
$(document).on('click', '#barber-get-appointments-btn', function () {
    const barberId = $('#barber-id').val();

    $.ajax({
        url: `http://127.0.0.1:8000/api/barber/${barberId}/appointments/`,
        method: 'GET',
        success: function (response) {
            // 处理预约列表数据
            console.log(response);
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 理发师审核预约
$(document).on('click', '#barber-approve-appointment-btn', function () {
    const appointmentId = $('#appointment-id').val();
    const isApproved = $('#is-approved').is(':checked');

    $.ajax({
        url: `http://127.0.0.1:8000/api/appointments/${appointmentId}/approve/`,
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            is_approved: isApproved
        }),
        success: function (response) {
            if (response.status === 'success') {
                alert('预约审核成功');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 理发师请假申请
$(document).on('click', '#barber-apply-leave-btn', function () {
    const barberId = $('#barber-id').val();
    const startTime = $('#start-time').val();
    const endTime = $('#end-time').val();
    const reason = $('#leave-reason').val();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/leave/create/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            barber: barberId,
            start_time: startTime,
            end_time: endTime,
            reason: reason
        }),
        success: function (response) {
            if (response.status === 'success') {
                alert('请假申请提交成功');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});