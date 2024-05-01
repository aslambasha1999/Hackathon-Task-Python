from datetime import datetime

def generate_html_report(feature_results, scenario_results,report_file_path):
    total_pass_count = 0
    total_fail_count = 0
    total_execution_time_ms = 0
    feature_execution_times = []
    pass_counts = []
    fail_counts = []
    #report_file_path = f"Reports/execution_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    with open(report_file_path, 'w') as report_file:
        report_file.write("<!DOCTYPE html>\n<html>\n<head>\n")
        report_file.write("<title>Execution Report</title>\n")
        report_file.write("<script src='https://cdn.jsdelivr.net/npm/chart.js'></script>\n")
        report_file.write("<style>\n")
        report_file.write("body { font-family: Arial, sans-serif; margin: 20px; }\n")
        report_file.write("table { border-collapse: collapse; width: 100%; }\n")
        report_file.write("th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }\n")
        report_file.write("th { background-color: #f2f2f2; }\n")
        report_file.write(".feature-link { text-decoration: none; }\n")
        report_file.write(".feature-pass { color: green; }\n")
        report_file.write(".feature-fail { color: red; }\n")
        report_file.write(".expand-icon, .collapse-icon { cursor: pointer; }\n")
        report_file.write("#myChart { max-width: 600px; margin-top: 20px; }\n")
        report_file.write("</style>\n")
        report_file.write("<script>\n")
        report_file.write("function toggleScenarioTable(index) {\n")
        report_file.write("    var table = document.getElementById('scenarioTable' + index);\n")
        report_file.write("    var icon = document.getElementById('toggleIcon' + index);\n")
        report_file.write("    if (table.style.display === 'none') {\n")
        report_file.write("        table.style.display = 'table';\n")
        report_file.write("        icon.classList.remove('fa-chevron-down');\n")
        report_file.write("        icon.classList.add('fa-chevron-up');\n")
        report_file.write("    } else {\n")
        report_file.write("        table.style.display = 'none';\n")
        report_file.write("        icon.classList.remove('fa-chevron-up');\n")
        report_file.write("        icon.classList.add('fa-chevron-down');\n")
        report_file.write("    }\n")
        report_file.write("}\n")
        report_file.write("</script>\n")
        report_file.write("</head>\n<body>\n")
        report_file.write("<h1>Execution Report</h1>\n")
        report_file.write(f"<p>Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>\n")

        report_file.write("<table>\n")
        report_file.write("    <tr>\n")
        report_file.write("        <th>Feature File</th>\n")
        report_file.write("        <th>Status</th>\n")
        report_file.write("        <th>Time Taken (ms)</th>\n")
        report_file.write("    </tr>\n")
        
        for index, (feature_file, status, execution_time) in enumerate(feature_results):
            scenario_times = [scenario_data[3] for scenario_data in scenario_results if scenario_data[0] == feature_file]
            total_scenario_time_ms = sum(scenario_times) * 1000
            total_execution_time_ms += total_scenario_time_ms
            report_file.write("    <tr>\n")
            report_file.write(f"        <td><a href=\"javascript:void(0)\" class='feature-link' onclick=\"toggleScenarioTable({index})\">{feature_file}</a><i id='toggleIcon{index}' class='expand-icon fas fa-chevron-down'></i></td>\n")
            if status.lower() == 'pass':
                report_file.write(f"        <td class='{'feature-pass' if status.lower() == 'pass' else 'feature-fail'}'>{status}</td>\n")
            else:
                report_file.write(f"        <td class='{'feature-pass' if status.lower() == 'pass' else 'feature-fail'}'>{status}</td>\n")
            report_file.write(f"        <td>{total_scenario_time_ms:.3f}</td>\n")
            report_file.write("    </tr>\n")
            report_file.write(f"<tr id=\"scenarioTable{index}\" style=\"display:none\">\n")
            report_file.write("        <td colspan=\"3\">\n")
            report_file.write("            <table align=\"center\">\n")
            report_file.write("                <tr>\n")
            report_file.write("                    <th>Scenario</th>\n")
            report_file.write("                    <th>Status</th>\n")
            report_file.write("                    <th>Time Taken (ms)</th>\n")
            report_file.write("                    <th>Remarks</th>\n")
            report_file.write("                </tr>\n")

            # Check if there are no scenarios found
            if not any(scenario_data[0] == feature_file for scenario_data in scenario_results):
                report_file.write("                <tr>\n")
                report_file.write("                    <td colspan=\"4\">No Scenarios Found</td>\n")
                report_file.write("                </tr>\n")
            else:
                # Iterate over scenarios and print them
                for scenario_data in scenario_results:
                    if scenario_data[0] == feature_file:
                        scenario_name = scenario_data[1]
                        scenario_status = scenario_data[2]
                        scenario_exec_time = scenario_data[3]
                        error_message = scenario_data[4] if len(scenario_data) >= 4 else ""  # Retrieve error message if available
                        report_file.write("                <tr>\n")
                        report_file.write(f"                    <td>{scenario_name}</td>\n")
                        if scenario_status.lower() == 'pass':
                            report_file.write(f"                    <td class='feature-pass'>{scenario_status}</td>\n")
                        else:
                            report_file.write(f"                    <td class='feature-fail'>{scenario_status}</td>\n")
                        report_file.write(f"                    <td>{scenario_exec_time * 1000:.3f}</td>\n")
                        report_file.write(f"                    <td>{': '.join(error_message.split(': ')[:-1])}</td>\n")  # Add Remarks column with error message
                        report_file.write("                </tr>\n")
                        report_file.write("                </tr>\n")

            report_file.write("            </table>\n")
            report_file.write("        </td>\n")
            report_file.write("    </tr>\n")

            
            if status.lower() == 'pass':
                total_pass_count += 1
            else:
                total_fail_count += 1
            

        
        report_file.write("</table>\n")
        report_file.write("<canvas id='myChart'></canvas>\n")
        report_file.write("<script>\n")
        report_file.write("var ctx = document.getElementById('myChart').getContext('2d');\n")
        report_file.write("var myChart = new Chart(ctx, {\n")
        report_file.write("    type: 'pie',\n")
        report_file.write("    data: {\n")
        report_file.write("        labels: ['Pass', 'Fail'],\n")
        report_file.write("        datasets: [{\n")
        report_file.write("            data: [")
        report_file.write(f"{total_pass_count}, {total_fail_count}")
        report_file.write("],\n")
        report_file.write("            backgroundColor: [\n")
        report_file.write("                'rgba(75, 192, 192, 0.5)',\n")
        report_file.write("                'rgba(255, 99, 132, 0.5)',\n")
        report_file.write("            ],\n")
        report_file.write("            borderColor: [\n")
        report_file.write("                'rgba(75, 192, 192, 1)',\n")
        report_file.write("                'rgba(255, 99, 132, 1)',\n")
        report_file.write("            ],\n")
        report_file.write("            borderWidth: 1\n")
        report_file.write("        }]\n")
        report_file.write("    },\n")
        report_file.write("    options: {\n")
        report_file.write("        responsive: false,\n")
        report_file.write("        maintainAspectRatio: false,\n")
        report_file.write("    }\n")
        report_file.write("});\n")
        report_file.write("</script>\n")
        report_file.write("<p style='font-weight: bold;'>Total Execution Time: ")
        if total_pass_count > 0:
            report_file.write(f"<span style='color: green;'>{total_execution_time_ms:.3f} milliseconds</span>")
        elif total_fail_count > 0:
            report_file.write(f"<span style='color: red;'>{total_execution_time_ms:.3f} milliseconds</span>")
        else:
            report_file.write(f"{total_execution_time_ms:.3f} milliseconds")
        report_file.write("</p>\n")
        report_file.write("</body>\n</html>\n")

    return report_file_path
