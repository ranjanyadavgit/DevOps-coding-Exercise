locals {
  users_list = ["user1:dev", "user2:prod", "user3:dev"]

  users_map = zipmap(
    [for u in local.users_list : split(":", u)[0]],
    [for u in local.users_list : split(":", u)[1]]
  )
}

output "debug" {
  value = "MAP_START${jsonencode(local.users_map)}MAP_END"
}
