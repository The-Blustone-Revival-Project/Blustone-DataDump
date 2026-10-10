# Actual SupplyFuel entry actions from healthy Village

2026-10-04. Read-only exact native caller instructions and selected UI LevelDB copy. No adb/Ghidra/source/client edits. Addresses are Ghidra code coordinates; vptrs explicitly use ELF VAs.

## Direct Village action — BT_ACTIVE

Use the **separate lower-right activity reward icon**, named **BT_ACTIVE**, with sprite **ACT_RW_ICON**. This is the actual free fuel popup route; the header AP meter BT_FUEL opens ShopFuel instead.

`CSRPopUpVillage::OnButtonClick` compares clicked object's CMHashID low32 **0x18b8c16a**, high32zero, at0xdad32e..0xdad33a. Shipped native literal BT_ACTIVE has standard CRC32=0x18b8c16a. On match:

```text
0xdad340 shared_ptr<CSRPopUpSupplyFuel>::make_shared (0x854540)
0xdad34e virtual Init(null)
0xdad352 CSRPopUpSupplyFuel::Reload (0xd719d0)
```

The parent/modal push is later in the same branch. No tutorial/state guard occurs between this button's hash match and Init/Reload; do not confuse it with achievement shortcut gates.

Selected seed contains both **EN/SR_MAIN/MAIN_ICON** and **KO/SR_MAIN/MAIN_ICON**, each25101 bytes, with the identical relevant subtree:

```xml
<panel name="PA_ACTIVE" pos="-128, -20" size="90, 90"
       align="right, bottom" visible="t">
  <button name="BT_ACTIVE" pos="0, 0" size="90, 90"
          align="center, center" event="pressed, release">
    <sprite res-name="ACT_RW_ICON" pos="0, 0"
            align="center, center" render-option="alphablend"/>
  </button>
</panel>
```

Those are layout units relative to its enclosing UI, **not asserted720x1280 screen coordinates**. Resolve its actual displayed icon/button bounds or existing UI node tree before tapping. Static visible=true is not proof a runtime ancestor stays visible, but a healthy Village's direct button handler is verified.

After opening it, bounded modal reader should see **SupplyFuel primary vptr B+0x2167d04**. Only then inspect framed view+0x98/root+8 and PA_CELL0/FuelCell template. If it still sees B+0x2166678, the action reached ShopFuel and has not tested SupplyFuel rendering.

## Other exact callers

`CSRAchieve::GoShortcut(string)`0x84dcb0 has a **SUPPLY_GET** shortcut branch. Input-string CRC compare0x84de96..0x84dea0 uses0xb5b586c4, which equals shipped SUPPLY_GET's standard CRC32; it branches0x84e152. It reads Tutorial.GetState(type0,step5) at0x84e190 and requires state>1 at0x84e196 before constructing SupplyFuel0x84e386, virtual Init0x84e392, Reload0x84e396, and modal push. This is an achievement route, not a free-standing shell command or invented deep link.

`CSRPopUpAchieve::OnButtonClick`0xb77e34 handles **BT_MOVE** (exact literal load0xb77f00/slot0xb781b4/add0xb77f08 resolves0x1d7c3e0). It takes current achievement's shortcut string at data+0x40, forms its CMHashID0xb77f36, compares SUPPLY_GET hash0xb5b586c4 at0xb77f62..0xb77f6e, then tests Tutorial type0/step5 at0xb78108..0xb7810e. On state>1, it constructs SupplyFuel0xb781ce, initializes, reloads and pushes. A meaningful existing achievement with shortcut SUPPLY_GET is required; an empty achievement list cannot provide this action merely because the callback exists.

These exactly attribute all three code callers of make_shared0x854540 in `ghidra-supply-fuel-entry-callers.txt`:0x84e386 GoShortcut,0xb781ce Achieve.OnButtonClick,0xdad340 Village.OnButtonClick. The direct **Village BT_ACTIVE** path is the shortest identified route from the current healthy UI and bypasses the need for reconstructed achievement contents.

Daily/calendar, NPC special list, and More fuel dialogue observations should remain separately attributed. None establishes entry into the free fuel scene without its actual SupplyFuel vptr. No new reference field, XML alias, or APK rebuild is required to test this proven Village button.
