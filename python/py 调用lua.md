```
import traceback
from lupa import LuaRuntime

fileHandler = open('test.lua')
content = ''
try:
	content = fileHandler.read()
except Exception as e:
	print(e)
	traceback.extract_stack()

# 创建lua执行环境
luaRuntime = LuaRuntime()
luaRuntime.execute(content)

# 从lua执行环境中取出全局函数functionCall作为入口函数调用,实现lua的反射调用
g = luaRuntime.globals()
function_call = g.functionCall
r1 = function_call('test1', "1111111111111111111111111111111111")
r2 = function_call('test2', "22222222222222222222")
print(r1)
print(r2)
print(g.aa)

```


```
function test1(params)
    return 'test1:'..params
end

function test2(params)
    return 'test2:'..params
end

-- 入口函数,实现反射函数调用
function functionCall(func_name,params)
    local is_true,result
    local sandBox = function(func_name,params)
        local result
        result = _G[func_name](params)
        return result
    end
    is_true,result= pcall(sandBox,func_name,params)
    return result
end
aa = 1200
```