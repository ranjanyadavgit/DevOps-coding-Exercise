# Terraform Local Map Creation

## 📌 Overview
This Terraform configuration transforms a list of `user:environment` pairs into a map where:
- **Keys** = usernames
- **Values** = their corresponding environments (`dev` or `prod`)

---

## 🛠️ Requirements
- Terraform **v0.12+**

---

## 📂 Code
```hcl
locals {
  users_list = ["user1:dev", "user2:prod", "user3:dev"]

  users_map = zipmap(
    [for user in local.users_list : split(":", user)[0]],
    [for user in local.users_list : split(":", user)[1]]
  )
}

output "debug" {
  value = "MAP_START${jsonencode(local.users_map)}MAP_END"
}
