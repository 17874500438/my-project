$(document).ready(function () {
    // 显示消费者登录页面
    $('#consumer-login-link').click(function () {
        showPage('consumer-login');
    });

    // 显示理发师登录页面
    $('#barber-login-link').click(function () {
        showPage('barber-login');
    });

    // 显示管理员登录页面
    $('#admin-login-link').click(function () {
        showPage('admin-login');
    });

    function showPage(pageId) {
        $.ajax({
            url: `D:/VScodecode/LF/pages/${pageId}.html`,
            success: function (data) {
                $('#page-content').html(data);
            },
            error: function () {
                alert('页面加载失败');
            }
        });
    }
});    