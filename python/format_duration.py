def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        sec_years = 60 * 60 * 24 * 365
        sec_days = 60 * 60 * 24
        sec_hours = 60 * 60
        sec_mins = 60
        years = seconds // sec_years
        rest_years = seconds % sec_years
        days = rest_years // sec_days
        rest_days = rest_years % sec_days
        hours = rest_days // sec_hours
        rest_hours = rest_days % sec_hours
        mins = rest_hours // sec_mins
        rest_mins = rest_hours % sec_mins
        secs = rest_mins % 60

        def string_format(x, y):
            return (x > 0) * (' ' + str(x) + ' ' + y + (x > 1) * 's')

        str_years = string_format(years, 'year')
        str_days = string_format(days, 'day')
        str_hours = string_format(hours, 'hour')
        str_mins = string_format(mins, 'minute')
        str_secs = string_format(secs, 'second')

        number = (years > 0) + (days > 0) + (hours > 0) + (mins > 0) + (secs > 0)
        inumber = number

        def format2(x, y):
            return x + (y > 0) * (',' * (inumber > 1) + ' and' * (inumber == 1))

        if (years > 0):
            inumber += -1
        str_years_final = format2(str_years, years)
        if (days > 0):
            inumber += -1
        str_days_final = format2(str_days, days)
        if (hours > 0):
            inumber += -1
        str_hours_final = format2(str_hours, hours)
        if (mins > 0):
            inumber += -1
        str_mins_final = format2(str_mins, mins)
        if (secs > 0):
            inumber += -1
        str_secs_final = format2(str_secs, secs)
        final = str_years_final + str_days_final + str_hours_final + str_mins_final + str_secs_final

        return final[1:]