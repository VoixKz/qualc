import { NavigationMenu, NavigationMenuItem, NavigationMenuLink, NavigationMenuList } from "@/components/ui/navigation-menu";

export function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-gray-900 text-white p-4">
      <NavigationMenu>
        <NavigationMenuList className="flex flex-col gap-4">
          <NavigationMenuItem>
            <NavigationMenuLink href="/" className="block p-2 rounded hover:bg-gray-700">Главная</NavigationMenuLink>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <NavigationMenuLink href="/dashboard" className="block p-2 rounded hover:bg-gray-700">Дэшборд</NavigationMenuLink>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <NavigationMenuLink href="/settings" className="block p-2 rounded hover:bg-gray-700">Настройки</NavigationMenuLink>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>
    </aside>
  );
}