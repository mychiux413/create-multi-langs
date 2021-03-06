// Package generated is automatically generated by `create-multi-langs`
package generated

// LangData fields are automatically generated from csv file
type LangData struct {
	SelectLang string // # select language
	Login      string // used for login button
	Hello      string // pop up greeting message
}

// LangCode restrict language code as type
type LangCode = string

var table = make(map[LangCode]LangData)

// LangCode List
const (
	ZHTW LangCode = "zh-tw"
	EN   LangCode = "en"
)

func init() {
	table[ZHTW] = LangData{
		SelectLang: "繁體中文",
		Login:      "登入",
		Hello:      "您好,歡迎",
	}
	table[EN] = LangData{
		SelectLang: "English",
		Login:      "Login",
		Hello:      "Hello,Welcome",
	}
}

// NewMultiLangs return language data for specific langCode
func NewMultiLangs(langCode LangCode) LangData {
	return table[langCode]
}

// SetLang set LangData's language code inplace
func (l *LangData) SetLang(langCode LangCode) {
	*l = table[langCode]
}
