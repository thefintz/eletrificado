<template>
  <div class="navbar-container">
    <Menubar :model="items" class="bg-gray-900 text-white navbar">
    </Menubar>
  </div>
</template>

<script setup lang="ts">
const router = useRouter();
const { signIn, signOut } = useAuth();

type Item = {
  label: string;
  icon: string;
  command: () => void;
};

const HOME: Item = {
  label: "Home",
  icon: "pi pi-home",
  command: () => router.push("/"),
};

const LOGIN: Item = {
  label: "Login",
  icon: "pi pi-sign-in",
  command: () => signIn("auth0"),
};

const PROFILE: Item = {
  label: "Profile",
  icon: "pi pi-user",
  command: () => router.push("/me"),
};

const LOGOUT: Item = {
  label: "Logout",
  icon: "pi pi-sign-out",
  command: () => signOut({ callbackUrl: "/" }),
};

const { status } = useAuth();
const items = ref<Item[]>([HOME, LOGIN]);
if (status.value === "authenticated") {
  items.value = [HOME, PROFILE, LOGOUT];
}
</script>

<style scoped>
.navbar {
  outline: none;
  border: none;
  box-shadow: none;
}

.navbar-container {
  padding: 0 20px;
}

.Menubar a {
  color: white;
}

.Menubar a:hover {
  color: #cbd5e0;
}
</style>
