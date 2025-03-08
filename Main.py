def analyze_shoes():
    # Collect inputs
    box_a_shoe1 = document.getElementById("box_a_shoe1").value.strip()
    box_a_shoe2 = document.getElementById("box_a_shoe2").value.strip()
    box_b_shoe1 = document.getElementById("box_b_shoe1").value.strip()
    box_b_shoe2 = document.getElementById("box_b_shoe2").value.strip()

    # Function to clean shoe data (removing markers)
    def clean_shoe(shoe):
        return shoe.replace('[', '').replace(']', '').replace('{', '').replace('}', '')

    # Step 1: Clean each shoe
    clean_box_a_shoe1 = clean_shoe(box_a_shoe1)
    clean_box_a_shoe2 = clean_shoe(box_a_shoe2)
    clean_box_b_shoe1 = clean_shoe(box_b_shoe1)
    clean_box_b_shoe2 = clean_shoe(box_b_shoe2)

    # Step 2: Identify markers in each shoe
    def track_markers(shoe):
        markers = {}
        count = 0
        skip_next = False
        for i, char in enumerate(shoe):
            if skip_next:
                skip_next = False
                continue
            if char in 'RB':
                marker = ''
                if i > 0 and shoe[i - 1] in '{[':
                    marker += shoe[i - 1]
                marker += char
                if i < len(shoe) - 1 and shoe[i + 1] in '}]':
                    marker += shoe[i + 1]
                skip_next = True
                if marker != char:
                    markers[count] = marker
                    count += 1
        return markers

    # Track markers for each shoe
    markers_a_shoe1 = track_markers(box_a_shoe1)
    markers_a_shoe2 = track_markers(box_a_shoe2)
    markers_b_shoe1 = track_markers(box_b_shoe1)
    markers_b_shoe2 = track_markers(box_b_shoe2)

    # Step 3: Combine markers for each shoe
    def combine_markers(markers_a, markers_b):
        combined = markers_b.copy()
        for key, value in markers_a.items():
            if key not in combined:
                combined[key] = value
        return combined

    combined_markers_shoe1 = combine_markers(markers_a_shoe1, markers_b_shoe1)
    combined_markers_shoe2 = combine_markers(markers_a_shoe2, markers_b_shoe2)

    # Step 4: Build the result shoe
    def build_result_shoe(clean_shoe, combined_markers):
        result = list(clean_shoe)
        for index, marker in combined_markers.items():
            result[index] = marker
        return ''.join(result)

    final_shoe1 = build_result_shoe(clean_box_b_shoe1, combined_markers_shoe1)
    final_shoe2 = build_result_shoe(clean_box_b_shoe2, combined_markers_shoe2)

    # Step 5: Display Results
    output = f"""
    Final Combined Shoe 1: {final_shoe1}
    Final Combined Shoe 2: {final_shoe2}
    """

    # ---------------- DEBUG OUTPUT ----------------
    debug_output = f"""
    --- DEBUG MODE ---
    Cleaned Box A Shoe 1: {clean_box_a_shoe1}
    Cleaned Box A Shoe 2: {clean_box_a_shoe2}
    Cleaned Box B Shoe 1: {clean_box_b_shoe1}
    Cleaned Box B Shoe 2: {clean_box_b_shoe2}
    Markers Box A Shoe 1: {markers_a_shoe1}
    Markers Box A Shoe 2: {markers_a_shoe2}
    Markers Box B Shoe 1: {markers_b_shoe1}
    Markers Box B Shoe 2: {markers_b_shoe2}
    Combined Markers Shoe 1: {combined_markers_shoe1}
    Combined Markers Shoe 2: {combined_markers_shoe2}
    """

    document.getElementById("output").value = output
    document.getElementById("debug_output").value = debug_output

# Run the analysis automatically on load
analyze_shoes()
