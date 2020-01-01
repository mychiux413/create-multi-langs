import { ml, setLang } from "./generated_frontend.mjs"

var compare = function(expect_value, actual_value) {
    if (expect_value !== actual_value) {
        return `[Error] expect '${expect_value}' but got '${actual_value}'\n`
    }
    return ""
}

var errs = ""
errs += compare(ml.Hello, "您好,歡迎")
errs += compare(ml.Login, "登入")
errs += compare(ml.SelectLang, "繁體中文")
setLang("en")
errs += compare(ml.Hello, "Hello,Welcome")
errs += compare(ml.Login, "Login")
errs += compare(ml.SelectLang, "English")

if (errs !== "") {
    throw errs
}