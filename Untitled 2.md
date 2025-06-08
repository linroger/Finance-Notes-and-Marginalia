$388/5= \frac{388}{5}=$$\frac{388}{5}$$$


```mermaid
graph TD
    subgraph Stage 0
        A0("Start")
    end

    subgraph Stage 1 (Interval 1)
        A1("✓ main <br/> 1/1 Segments")
    end

    subgraph Stage 2 (Interval 2)
        B1("✓ main_variant_1_1")
        B2("✓ main_variant_2_1")
        B3("⏳ main_variant_3_1")
    end

    subgraph Stage 3 (Interval 3)
        C1("✓ All descendants complete <br/> (3 Segments)")
        C2("✓ All descendants complete <br/> (3 Segments)")
        C3("✓ ...variant_1_2")
        C4("✓ ...variant_2_2")
        C5("⏳ ...variant_3_2")
    end

    subgraph Stage 4 (Interval 4)
        D1("✓ All descendants complete <br/> (9 Segments)")
        D2("✓ All descendants complete <br/> (9 Segments)")
        D3("⏳ ...variant_1_3")
        D4("⚪ ...variant_2_3")
        D5("⚪ ...variant_3_3")
    end

    subgraph Stage 5 (Interval 5)
        E1("✓ Final 27 Segments")
        E2("✓ Final 27 Segments")
        E3("✓ Final 9 Segments")
        E4("✓ Final 9 Segments")
        E5("<b>In Progress: 3 Segments</b>")
        E6("<b>Pending: 3 Segments</b>")
        E7("<b>Pending: 3 Segments</b>")
    end
    
    A0 -- ✓ 1/1 --▷ A1
    
    A1 --▷ B1
    A1 --▷ B2
    A1 --▷ B3
    
    B1 --▷ C1
    B2 --▷ C2
    B3 --▷ C3
    B3 --▷ C4
    B3 --▷ C5
    
    C1 --▷ E1
    C2 --▷ E2
    C3 --▷ D1
    C4 --▷ D2
    
    D1 --▷ E3
    D2 --▷ E4
    
    C5 --▷ D3
    C5 --▷ D4
    C5 --▷ D5
    
    D3 --▷ E5
    D4 --▷ E6
    D5 --▷ E7

    style E5 fill:#f9f,stroke:#333,stroke-width:2px
    style E6 fill:#f9f,stroke:#333,stroke-width:2px
    style E7 fill:#f9f,stroke:#333,stroke-width:2px
```

