function PrintTable(t)
    for key, value in pairs(t) do
      if type(value) == "table" then
        print(key .. ":")
        PrintTable(value)
      else
        print(key, value)
      end
    end
  end

  -- 导入必要的组件库
local component = require("component")
local me = component.me_controller
PrintTable(me)
-- 获取所有ME网络中的CPU信息
local cpus = me.getCpus()

-- 遍历并打印每个CPU的信息
for i, cpu in ipairs(cpus) do
  print("CPU " .. i .. ":")
  print("Name: " .. (cpu.name or "N/A"))
  print("Available: " .. tostring(cpu.isAvailable))
  print("Storage: " .. cpu.storage .. " bytes")
  print("Co-Processors: " .. cpu.coprocessors)
  print("-----")
end
