module main

import os
import cli
import pacman


fn main() {
    mut app := cli.Command{
        name: 'pacv'
        description: 'Wrapper for pacman package manager'
        version: '5.0.0'
        execute: fn (cmd cli.Command) ? {
            println("Wrong usage. Run with --help flag to see current commands.")
            return
        }
        commands: [
            cli.Command{
                name: 'install'
                description: 'Install the desired package'
                execute: fn (cmd cli.Command) ? {
                    pacman.install()
                    return
                }
            }
            cli.Command{
                name: 'remove'
                description: 'Remove the desired package'
                execute: fn (cmd cli.Command) ? {
                    pacman.remove()
                    return
                }
            }
            cli.Command{
                name: 'update'
                description: 'Updates the system'
                execute: fn (cmd cli.Command) ? {
                    pacman.upgrade()
                    return
                }
            }
            cli.Command{
                name: 'orphans'
                description: 'Remove orphaned packages'
                execute: fn (cmd cli.Command) ? {
                    os.system("sudo pacman -R $(pacman -Qqdt)")
                    return
                }
            }
            cli.Command{
                name: 'search'
                description: 'Search for packages'
                execute: fn (cmd cli.Command) ? {
                    pacman.search()
                    return
                }
            }
            cli.Command{
                name: 'info'
                description: 'Information of packages'
                execute: fn (cmd cli.Command) ? {
                    pacman.info()
                    return
                }
            }
            cli.Command{
                name: 'refresh'
                description: 'Refresh repository info'
                execute: fn (cmd cli.Command) ? {
                    pacman.refresh()
                    return
                }
            }
        ]
    }
    app.setup()
    app.parse(os.args)
}