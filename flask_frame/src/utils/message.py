# 状态码与提示映射
from utils.codes import (
    CODE_BAD_REQUEST,
    CODE_UNAUTHORIZED,
    CODE_FORBIDDEN,
    CODE_NOT_FOUND,
    CODE_SERVER_ERROR,
    BIZ_CODE_OK,
    BIZ_CODE_FAIL,
    BIZ_CODE_NOT_EXISTS
)

errmsg = {
    CODE_BAD_REQUEST: "参数错误",
    CODE_UNAUTHORIZED: "权限不足",
    CODE_FORBIDDEN: "拒绝访问",
    CODE_NOT_FOUND: "无法找到资源",
    CODE_SERVER_ERROR: "服务端错误",
    BIZ_CODE_OK: "成功",
    BIZ_CODE_FAIL: "失败",
    BIZ_CODE_NOT_EXISTS: "对象不存在"
}
