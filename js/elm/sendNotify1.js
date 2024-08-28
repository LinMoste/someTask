
async function sendNotify(
    text,
    desp,
    params = {},
    author = '\n\n关注飞机频道：https://t.me/tigerorrose，及时获取脚本更新信息',
) {
    //提供6种通知
    if (process.env.pushDesc){
        author = '\n\n' + process.env.pushDesc;
    }
    desp += author; //增加作者信息，防止被贩卖等
    await Promise.all([
        // serverNotify(text, desp), //微信server酱
        // pushPlusNotify(text, desp), //pushplus(推送加)
        QLAPI.notify(text,desp)
        // tgBotNotify(text,desp),
        // wxPushNotify(text, desp, params) //wxPush
    ]);

}




