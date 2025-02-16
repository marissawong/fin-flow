import { UserRaw } from "@/app/models"
import { sql } from "@vercel/postgres"

const user = await sql<UserRaw>`
  select
    user_id,
    name,
    email
  from users`

export async function fetchUserData() {
  try {
    return user
  } catch (error) {
    console.error("Failed to fetch user data", error)
  }
}
