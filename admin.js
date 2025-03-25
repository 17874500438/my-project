// 管理员登录
$(document).on('click', '#admin-login-submit-btn', function () {
    const account = $('#admin-account').val();
    const password = $('#admin-password').val();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/admin/login/',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            account: account,
            password: password
        }),
        success: function (response) {
            if (response.status === 'success') {
                showPage('admin-home');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 管理员获取请假申请列表
$(document).on('click', '#admin-get-leaves-btn', function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/admin/leaves/',
        method: 'GET',
        success: function (response) {
            // 处理请假申请列表数据
            console.log(response);
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 管理员审批请假申请
$(document).on('click', '#admin-approve-leave-btn', function () {
    const leaveId = $('#leave-id').val();
    const isApproved = $('#is-approved').is(':checked');

    $.ajax({
        url: `http://127.0.0.1:8000/api/admin/leaves/${leaveId}/approve/`,
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            is_approved: isApproved
        }),
        success: function (response) {
            if (response.status === 'success') {
                alert('请假申请审批成功');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 管理员获取反馈列表
$(document).on('click', '#admin-get-feedbacks-btn', function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/admin/feedbacks/',
        method: 'GET',
        success: function (response) {
            // 处理反馈列表数据
            console.log(response);
        },
        error: function () {
            alert('请求失败');
        }
    });
});

// 管理员处理反馈
$(document).on('click', '#admin-handle-feedback-btn', function () {
    const feedbackId = $('#feedback-id').val();

    $.ajax({
        url: `http://127.0.0.1:8000/api/admin/feedbacks/${feedbackId}/handle/`,
        method: 'POST',
        success: function (response) {
            if (response.status === 'success') {
                alert('反馈处理成功');
            } else {
                alert(response.message);
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
});