# Returning Icons in Conditional Formatting

Instead of returning colours, you can return items as conditional formating in PowerBI. 

**Example DAX**

```
Target FTE Background = 
VAR _FTE = SUM(FTE[FTE])
VAR _TargetFTE = SUM(Targets[Target FTE])

RETURN

SWITCH(
    TRUE(),
    _FTE > _TargetFTE, "CircleHigh",
    _FTE < _TargetFTE, "CircleLow", 
    "White"
)
```

This code returns either a green circle if the FTE value is greater than Target, or a red circle if it is below. Else white. 

**List**

- SignLow
- SignMedium
- CircleHigh
- CircleMedium
- CircleLow
- 4CircleLow
- CircleMedium1
- 4CircleMedium2
- CircleEmpty
- Circle25
- CircleHalf
- Circle75
- CircleFilled
- TrafficLow
- TrafficMedium
- TrafficHigh
- TrafficBlackRimmed
- TrafficLowLight
- TrafficMediumLight
- TrafficHighLight
- TrafficBlackRimmedLight
- ColoredArrowDownRight
- ColoredArrowRight
- ColoredArrowUpRight
- ColoredArrowUp
- GreyArrowDown
- GreyArrowDownRight
- GreyArrowRight
- GreyArrowUpRight
- GreyArrowUp
- FlagLow
- FlagMedium
- FlagHigh
- FlagBlack
- SymbolLow
- SymbolMedium
- SymbolHigh
- CircleSymbolLow
- CircleSymbolMedium
- CircleSymbolHigh
- StarLow
- StarMedium
- StarHigh
- StarMediumLight
- StarHighLight
- TriangleLow
- TriangleMedium
- TriangleHigh
- SignalBarEmpty
- SignalBarLow
- SignalBarMedium
- SignalBarMedium2
- SignalBarFull
- SignalBarLowColored
- SignalBarMediumColored
- SignalBarMedium2Colored
- SignalBarFullColored
- QuadrantEmpty
- Quadrant25
- Quadrant50
- Quadrant75
- QuadrantFull
- Quadrant25Colored
- Quadrant50Colored
- Quadrant75Colored
- QuadrantFullColored