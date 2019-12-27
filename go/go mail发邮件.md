```go
package service

import (
	"crypto/tls"
	"fmt"
	"net"
	"net/smtp"
	"strings"
)

func (this *Service) SendMail(body string) (err error) {
	toEmailList := []string{"1034455262@qq.com"}

	host := "smtp.mxhichina.com"
	port := 465
	email := "发送的邮箱"                     // 发送邮箱
	pwd := "密码"                             // 邮箱密码
	toEmail := strings.Join(toEmailList, ";") // 目标地址
	header := make(map[string]string)
	header["From"] = "自动化" + "<" + email + ">"
	header["To"] = strings.Join(toEmailList, "")
	header["Subject"] = "自动化申请通知"
	header["Content-Type"] = "text/html;charset=UTF-8"
	message := ""
	for k, v := range header {
		message += fmt.Sprintf("%s:%s\r\n", k, v)
	}
	message += "\r\n" + body
	auth := smtp.PlainAuth(
		"",
		email,
		pwd,
		host,
	)
	err = SendMailUsingTLS(
		fmt.Sprintf("%s:%d", host, port),
		auth,
		email,
		toEmail,
		[]byte(message),
	)
	if err != nil {
		this.Log.Info("发送邮件失败!")
		this.Log.Info(err)
	} else {
		fmt.Println("发送邮件成功!")
	}
	return
}
func SendMailUsingTLS(addr string, auth smtp.Auth, from string, to string, msg []byte) (err error) {
	c, err := Dial(addr)
	if err != nil {
		return err
	}
	defer c.Close()
	if auth != nil {
		if ok, _ := c.Extension("AUTH"); ok {
			if err = c.Auth(auth); err != nil {
				return err
			}
		}
	}
	if err = c.Mail(from); err != nil {
		return err
	}
	tos := strings.Split(to, ";")
	for _, addr := range tos {
		if err = c.Rcpt(addr); err != nil {
			fmt.Print(err)
			return err
		}
	}
	w, err := c.Data()
	if err != nil {
		return err
	}
	_, err = w.Write(msg)
	if err != nil {
		return err
	}
	err = w.Close()
	if err != nil {
		return err
	}
	return c.Quit()
}
func Dial(addr string) (*smtp.Client, error) {
	//conn, err := tls.Dial("tcp", addr, nil)
	conn, err := tls.Dial("tcp", addr, &tls.Config{InsecureSkipVerify: true})
	if err != nil {
		return nil, err
	}
	//分解主机端口字符串
	host, _, _ := net.SplitHostPort(addr)
	return smtp.NewClient(conn, host)
}

```
