<template>
    <Menubar :model="items">
      <template #item="{ item, props }">
        <a v-ripple v-bind="props.action">
            <span :class="item.icon" />
            <span>{{ item.label }}</span>
        </a>
      </template>
    </Menubar>
</template>

<script setup lang="ts">
const router = useRouter();
const { signIn, signOut } = useAuth();

type Item = {
  label: string;
  icon: string;
  command: () => void;
};

const LOGIN: Item = {
  label: "Entrar",
  icon: "pi pi-sign-in",
  command: () => signIn("auth0"),
};

const PROFILE: Item = {
  label: "Perfil",
  icon: "pi pi-user",
  command: () => router.push("/me"),
};

const LOGOUT: Item = {
  label: "Sair",
  icon: "pi pi-sign-out",
  command: () => signOut({ callbackUrl: "/" }),
};

const { status } = useAuth();
const items = ref<Item[]>([LOGIN]);
if (status.value === "authenticated") {
  items.value = [PROFILE, LOGOUT];
}
</script>

<style scoped>
.p-menubar {
    background: transparent;
    border: none;
}
</style>